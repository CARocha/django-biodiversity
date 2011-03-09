from pygooglechart import PieChart3D, PieChart2D 
from pygooglechart import StackedHorizontalBarChart, StackedVerticalBarChart
from pygooglechart import GroupedHorizontalBarChart, GroupedVerticalBarChart
from pygooglechart import Axis, SimpleLineChart
from django.utils import simplejson
from django.http import HttpResponse
from settings import NO_DATA_GRAPH_URL

pie_types = [PieChart3D, PieChart2D]
bar_types = [StackedHorizontalBarChart, StackedVerticalBarChart,
             GroupedHorizontalBarChart, GroupedVerticalBarChart]
line_types = [SimpleLineChart]

PIE_CHART_3D, PIE_CHART_2D = pie_types
BAR_CHART_H, BAR_CHART_V, GROUPED_BAR_CHART_H, GROUPED_BAR_CHART_V = bar_types
LINE_CHART = line_types

COLORS = ['FFBC13','22A410','E6EC23','2B2133','BD0915','3D43BD','003366','0197fd','d40000','6600cc','c17d11','3465a4','fcaf3e','75507b','8ae234']

def make_graph(data, legends, message=None, 
               axis_labels=None, steps=4, return_json = False,
               type=PieChart2D, size=(920, 300), multiline=False, **kwargs):

    if (type in pie_types):
        graph = _pie_graph(data, legends, size, type)
    elif (type in bar_types):
        graph = _bar_graph(data, legends, axis_labels, size,
                               steps, type, multiline)
    elif(type is line_types):
        graph = _line_strip_graph(data, legends, axis_labels,
                                       size, steps, type, multiline, **kwargs)
    else:
        raise Exception('shit broke')
    try:
        graph.set_title(message)
        url = graph.get_url()
    except Exception as e:
        url = NO_DATA_GRAPH_URL 


    if return_json:

        dicc = {'url': url}
        return HttpResponse(simplejson.dumps(dicc), mimetype='application/javascript')
    else:
        return url 


def _pie_graph(data, legends, size, type=PieChart3D):
    graph = type(size[0], size[1])
    graph.set_colours(COLORS)
    graph.add_data(data)
    graph.set_legend(legends)
    porcentajes = saca_porcentajes(data)
    graph.set_pie_labels(porcentajes)
    graph.set_legend_position("b")

    return graph

def _bar_graph(data, legends, axis_labels, size, steps,  
                    type=StackedVerticalBarChart, multiline=False):
    
    if multiline:
        max_values = []
        min_values = [] 
        for row in data:
            max_values.append(max(row))
            min_values.append(min(row))
        max_value = max(max_values)
        min_value = min(min_values)
    else:
        max_value = max(data)
        min_value = min(data)

    #validando si hay datos para hacer grafico
    if max_value==0:
        return None

    step = ((max_value*1.05)-(min_value*0.95))/steps
    
    #validando en caso de el paso sea menor que uno y de cero en la conversion
    if step<1:
        step = 1    

    tope = int(round(max_value*1.05))
    if tope < max_value:
        tope+=2
    else:
        tope+=1

    left_axis = range(int(round(min_value*0.95)), tope, int(step))
    left_axis[0]=''

    if type==StackedHorizontalBarChart:
        graph = StackedHorizontalBarChart(size[0], size[1], x_range=(0, max_value*1.05))
        graph.set_axis_labels(Axis.BOTTOM, left_axis)
        if axis_labels:
            graph.set_axis_labels(Axis.LEFT, axis_labels)
    elif type==StackedVerticalBarChart:
        graph = StackedVerticalBarChart(size[0], size[1], y_range=(0, max_value*1.05))
        graph.set_axis_labels(Axis.LEFT, left_axis)
        if axis_labels:
            graph.set_axis_labels(Axis.BOTTOM, axis_labels)
    elif type==GroupedHorizontalBarChart:
        graph = GroupedHorizontalBarChart(size[0], size[1], x_range=(0, max_value*1.05))
        graph.set_axis_labels(Axis.BOTTOM, left_axis)
        if axis_labels:
            graph.set_axis_labels(Axis.LEFT, axis_labels)
        graph.set_bar_spacing(5)
    elif type==GroupedVerticalBarChart:
        graph = GroupedVerticalBarChart(size[0], size[1], y_range=(0, max_value*1.05))
        graph.set_axis_labels(Axis.LEFT, left_axis)
        if axis_labels: 
            graph.set_axis_labels(Axis.BOTTOM, axis_labels)
        graph.set_bar_spacing(5)
    else:
        pass #raise exception


    if multiline:
        for fila in data:
            graph.add_data(fila)
    else:
        graph.add_data(data)
    
    graph.set_colours(COLORS)
    graph.set_bar_width(44)
    graph.set_legend(legends)
    graph.set_legend_position('b')
    
    
    return graph

def _line_strip_graph(data, legends, axis_labels, size, steps, 
                           type=SimpleLineChart, multiline=False, **kwargs):
    if multiline:
        max_values = []
        min_values = [] 
        for row in data:
            max_values.append(max(row))
            min_values.append(min(row))
        max_y = max(max_values)
        min_y = min(min_values)
    else:
        max_y = max(data)
        min_y = min(data)
    
    #validando si hay datos para hacer grafico
    if max_y==0:
        return None

    chart = SimpleLineChart(size[0], size[1], y_range=[0, max_y*1.05])

    if multiline:
        for row in data:
            chart.add_data(row)
    else:
        chart.add_data(data)
    
    step = ((max_y*1.05)-(min_y*0.95))/steps

    #validando en caso de el paso sea menor que uno y de cero en la conversion
    if step<1:
        step = 1
    
    max_value = max_y
    tope = int(round(max_value*1.05))
    if tope < max_value:
        tope+=2
    else:
        tope+=1

    try:
        left_axis = range(int(round(min_y*0.95)), tope, int(step))
    except ValueError:
        #error por que los range no soportan decimales
        left_axis = range(0, 2)
    left_axis[0]=''

    chart.set_axis_range(Axis.LEFT, min_y, tope)
    if 'units' in kwargs:
        chart.set_axis_labels(Axis.LEFT, kwargs['units'])
    chart.set_grid(0, 25, 4, 4,)
    chart.chls=4|4
    #chart.fill_linear_stripes(Chart.CHART, 0, 'FFFFEF', 0.2, 'FFFFFF', 0.2)
    chart.set_colours(COLORS)

    if axis_labels:
        chart.set_axis_labels(Axis.BOTTOM, axis_labels)
    chart.set_legend(legends)
    chart.set_legend_position('b')

    if 'thickness' in kwargs:
        if multiline:
            for i in range(len(data)):
                chart.set_line_style(index = i, thickness=kwargs['thickness'])
        else:
            chart.set_line_style(index=0, thickness=kwargs['thickness'])

    return chart


def saca_porcentajes(values):
    """sumamos los valores y devolvemos una lista con su porcentaje"""
    total = sum(values)
    valores = [] 
    for i in range(len(values)):
        if total!=0:
            porcentaje = (float(values[i])/total)*100
        else:
            porcentaje = 0
        valores.append("%.2f" % porcentaje + '%')
    return valores
