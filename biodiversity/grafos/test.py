import grafos
from pygooglechart import StackedHorizontalBarChart, StackedVerticalBarChart, GroupedHorizontalBarChart, GroupedVerticalBarChart 

def run():
    data = [[100,200,150,120],[120, 90, 80, 40]]
    legends = ['mujeres', 'hombres']
    message = 'titulo ejemplo'
    axis = ['1990', '1991', '1992', '1993']
    print 'grafo horizontal apliado'
    print grafos.make_graph(data, legends, message, axis, size=(500,500),
                            multiline=True,
                      return_json=False, type=StackedHorizontalBarChart)
    print 'grafo vertical apliado'
    print grafos.make_graph(data, legends, message, axis, size=(500,500),
                            multiline=True,
                      return_json=False, type=StackedVerticalBarChart)

    print 'grafo horizontal agrupado'
    print grafos.make_graph(data, legends, message, axis, size=(500,500),
                            multiline=True,
                      return_json=False, type=GroupedHorizontalBarChart)
    print 'grafo vertical apliado'
    print grafos.make_graph(data, legends, message, axis, size=(500,500),
                            multiline=True,
                      return_json=False, type=GroupedVerticalBarChart)
if __name__ == "__main__":
    run()
