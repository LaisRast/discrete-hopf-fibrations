# Discrete Hopf Fibrations

This gallery shows polar orbit polytopes for the cyclic-type tubical groups
with all choices of special starting points. It is based on the article
[Towards a Geometric Understanding of the 4-Dimensional Point
Groups](http://arxiv.org/abs/2205.04965) by Laith Rastanawi and Günter Rote.

The main goal of the gallery is to show cell decomposition of these polytopes
into tubes (discrete Hopf fibrations), and how these tubes are structured and
interact with each other.

## Running

You can view the gallery live
[here](https://www.inf.fu-berlin.de/inst/ag-ti/software/DiscreteHopfFibration/).
Alternatively you can run it independently:

* Clone this repository:
  ```
  git clone https://github.com/LaisRast/discrete-hopf-fibrations.git
  ```

* Generate tubes data (~75.8MiB) by running the script `generate_tubes.sage`
  which you can find [here](https://github.com/LaisRast/point-groups):
  ```
  sage generate_tubes.sage
  ```
  Note that this is a [Sage](https://www.sagemath.org/) script, and you need to
  [install the Normaliz
  backend](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/polyhedron/backend_normaliz.html)
  to run it. The script will generate the data and put them in `data/`
  directory. Copy that directory into the cloned repository.

* Generate the file `files.json`:
  ```
  python3 generate_file_list.py
  ```

* Run a local server in the cloned repository:
  ```
  python3 -m http.server
  ```
  and access the gallery through [http://0.0.0.0:8000/](http://0.0.0.0:8000/).


## Used Libraries

* [RainbowVis-JS](https://github.com/anomal/RainbowVis-JS):
  A JavaScript library for colour data visualization. [EPL-1.0]
  
* [three.js](https://github.com/mrdoob/three.js/):
  A JavaScript 3D library. [MIT]
  
* [Pico.css](https://github.com/picocss/pico):
  Minimal CSS Framework for semantic HTML. [MIT]
