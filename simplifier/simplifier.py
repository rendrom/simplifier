import geopandas
import topojson


class Simplifier:
    def __init__(self,
                 input_file,
                 simplify=4,
                 output_format='geojson'
                 ):
        self.input_file = input_file
        self.simplify = simplify
        self.output_format = output_format

    def run(self):
        data = geopandas.read_file(self.input_file)
        topo = topojson.Topology(data, toposimplify=self.simplify)

        return topo.to_geojson()
