/*
 * Copyright 2018 <copyright holder> <email>
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "graph_edge.h"
#include "graph_node.h"
#include <qmath.h>
#include <QPainter>
#include <QDebug>
#include "../../dsr_gui.h"
#include <QGraphicsSceneMouseEvent>
#include <iostream>
#include <cppitertools/range.hpp>

GraphEdge::GraphEdge(GraphNode *sourceNode, GraphNode *destNode, const QString &edge_name) : QGraphicsLineItem(), arrowSize(10)
{
    setFlags(QGraphicsItem::ItemIsSelectable);
	setFlag(QGraphicsItem::ItemIsFocusable);
    source = sourceNode;
    dest = destNode;
    source->addEdge(this);
    dest->addEdge(this);
	tag = edge_name;
	if (edge_name == "RT") {
        color = "black";
    }
    else {
        color = "red";
    }
	animation = new QPropertyAnimation(this, "edge_pen");
	animation->setDuration(200);
	animation->setStartValue(4);
	animation->setEndValue(2);
	animation->setLoopCount(3);
	adjust();
    QObject::connect(source->getGraphViewer()->getGraph().get(), &DSR::DSRGraph::update_edge_attr_signal, this, &GraphEdge::update_edge_attr_slot);
}

GraphNode *GraphEdge::sourceNode() const
{
    return source;
}

GraphNode *GraphEdge::destNode() const
{
    return dest;
}

void GraphEdge::adjust(GraphNode* node, QPointF pos)
{
    if(!source || !dest)
		return;

	QLineF *line;
    if(node) {
		if (node==source) {
			line = new QLineF(pos, mapFromItem(dest, 0, 0));
		}
		else {
			line = new QLineF(mapFromItem(source, 0, 0), pos);
		}
	}
	else
	{
		line = new QLineF(mapFromItem(source, 0, 0), mapFromItem(dest, 0, 0));
	}


    qreal length = line->length();

    prepareGeometryChange();

    if (length > qreal(20.)) 
		{
        QPointF edgeOffset((line->dx() * 10) / length, (line->dy() * 10) / length);
        sourcePoint = line->p1() + edgeOffset;
        destPoint = line->p2() - edgeOffset;
    } else {
		sourcePoint = destPoint = line->p1();
	}
    delete line;
}

QRectF GraphEdge::boundingRect() const
{
	QLineF line(sourcePoint, destPoint);

	return QRectF(sourcePoint, destPoint).normalized().adjusted(-10,-10, +10, +10);

}

QPainterPath GraphEdge::shape() const
{
    QPainterPath path;
    path.addPolygon(tag_polygon);
    return path;
}


void GraphEdge::paint(QPainter *painter, const QStyleOptionGraphicsItem *, QWidget *)
{
    if (!source || !dest)
        return;

    QLineF line(sourcePoint, destPoint);
		
		// self returning edges
    if (qFuzzyCompare(line.length(), qreal(0.)))
		{
				// Draw the line itself
				painter->setPen(QPen(color, edge_width, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
				QRectF rectangle(sourcePoint.x()-20, sourcePoint.y()-20, 20.0, 20.0);
				int startAngle = 35;
				int spanAngle = 270 * 16;
				painter->drawArc(rectangle, startAngle, spanAngle);
				painter->setPen(QColor("coral"));
				painter->drawText(rectangle.center(), tag);
				double alpha = 0;
				double r = 20/2.f;
				painter->setBrush(color);
				painter->setPen(QPen(color, edge_width));
				painter->drawPolygon(QPolygonF() << QPointF(r*cos(alpha) + rectangle.center().x(), r*sin(alpha) + rectangle.center().y())
																				 << QPointF(r*cos(alpha) + rectangle.center().x()-3, r*sin(alpha) + rectangle.center().y()-2) 
																				 << QPointF(r*cos(alpha) + rectangle.center().x()+2, r*sin(alpha) + rectangle.center().y()-2));
		}
		else
		{
			//check if there is another parallel edge 
			// Draw the line itself

			painter->save();
			painter->setPen(QPen(color, edge_width, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
			double angle = std::atan2(-line.dy(), line.dx());
			painter->translate(line.center().x(), line.center().y());
			painter->rotate(-angle*180/M_PI);
			QRectF rectangle(-line.length()*0.5, -10, line.length(), 20);
			painter->drawArc(rectangle, 0, 180*16);


			painter->setPen(QColor("coral"));
			painter->drawText(rectangle.center(), tag);
			auto fm = QFontMetrics(painter->font());
			auto tag_rect = QRectF(-5,(-fm.height()-10)*0.5, fm.width(tag)+10, fm.height()+10);
			tag_polygon = QTransform()
					.translate(line.center().x(), line.center().y())
					.rotate(-angle*180/M_PI)
					.map(QPolygonF(tag_rect));

				
			// Draw the arrows
			QPointF destArrowP1 = QPointF(line.length()*0.5,0) - QPointF(sin(M_PI / 2) * arrowSize, cos(M_PI / 2) * arrowSize);
			QPointF destArrowP2 = QPointF(line.length()*0.5,0) - QPointF(sin(M_PI / 4) * arrowSize, cos(M_PI / 4) * arrowSize);
			painter->setBrush(color);
			painter->setPen(QPen(color, edge_width));
			painter->drawPolygon(QPolygonF() << QPointF(line.length()*0.5,0) << destArrowP1 << destArrowP2 );
			painter->setPen(pen());

			painter->restore();
//			// DEBUG
//			painter->setBrush(QBrush(Qt::red));
//			painter->drawRect(boundingRect());
//			painter->drawEllipse(line.p1(), 5, 5);
//			painter->drawEllipse(line.p2(), 5, 5);
//			painter->drawPolygon(tag_polygon);
//			painter->setBrush(QBrush(Qt::black));
//			if (true) {
//				painter->setBrush(QBrush(QColor(128, 128, 255, 128)));
//				painter->setPen(QPen(Qt::black, 2, Qt::DashLine));
//				painter->drawPath(this->shape());
//			}
		}
	
}


void GraphEdge::mouseDoubleClickEvent(QGraphicsSceneMouseEvent* event)
{
	qDebug() << __FILE__ << " " << __FUNCTION__ << "Edge from " << source->id_in_graph << " to " << dest->id_in_graph <<" tag: " << tag ;
	static std::unique_ptr<QWidget> do_stuff;
	const auto graph = source->getGraphViewer()->getGraph();
	if( event->button()== Qt::RightButton)
	{
		if(tag == "RT" or tag == "looking-at")
			do_stuff = std::make_unique<DoRTStuff2>(graph, source->id_in_graph, dest->id_in_graph, tag.toStdString());
	}
	animation->start();
	update();
	QGraphicsLineItem::mouseDoubleClickEvent(event);
}





void GraphEdge::keyPressEvent(QKeyEvent *event) 
{
    if (event->key() == Qt::Key_Escape)
    {
        if(label != nullptr)
        {
            label->close();
            delete label; 
            label = nullptr;
        }
    }
}

void GraphEdge::change_detected()
{
	animation->start();
}


int GraphEdge::_edge_pen()
{
	return this->edge_width;
}

void GraphEdge::set_edge_pen(const int p)
{
	this->edge_width = p;
	this->setPen(QPen(Qt::black, edge_width, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
}


void GraphEdge::update_edge_attr_slot(std::uint64_t from, std::uint64_t to, const std::vector<std::string>& att_name)
{
    if ((from != this->source->id_in_graph) or (to != this->dest->id_in_graph))
        return;
    if(std::find(att_name.begin(), att_name.end(), "color") != att_name.end())
    {
        std::optional<Edge> edge = source->getGraphViewer()->getGraph()->get_edge(from, to, tag.toStdString());
        if (edge.has_value()) {
            auto &attrs = edge.value().attrs();
            auto value = attrs.find("color");
            if (value != attrs.end()) {
                this->color = QColor(QString::fromStdString(value->second.str()));
            }
        }
    }
}
