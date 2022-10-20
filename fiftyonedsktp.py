import fiftyone as fofo
import fiftyone.zoo as fozoo

dataset = fozoo.load_zoo_dataset("quickstart", "quickstart_2")
session = fofo.launch_app(dataset, port=5500)