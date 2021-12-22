# Venetian-Bridges
Venice 1808: Upgrading the bridge with 3D models

More detailed info on the wiki page: http://fdh.epfl.ch/index.php/3DVeniceBirdges

Venice is built on a group of 118 small islands that are separated by canals and linked by over 400 bridges. Venice is built on a group of 118 small islands that are separated by canals and linked by over 400 bridges. The Bridge plays such an important part in Venice that studying the bridge can help us understand better the history and structure of Venice. Our project is mainly based on the book [Catalogo Veneziano – Ponti Santa Croce](https://studiosaor.com/product/catalogo-veneziano-ponti-santa-croce/) and [Catalogo Veneziano – Ponti San Polo](https://studiosaor.com/product/catalogo-veneziano-ponti-san-polo/), to build specific 3D models for these bridges and to create specific additional layers on the geographical information system.

####  

#### JSON FILE FORMAT:

|  column   | description                                                  |
| :-------: | ------------------------------------------------------------ |
|    id     | The unique id of each bridge                                 |
|  id_book  | The id used in the book *Catalogo Veneziano*                 |
|   name    | The name of the bridge                                       |
|   river   | The river which the bridge crosses                           |
|  street   | The street connected by this bridge                          |
| district  | The community where the bridge is located                    |
| structure | The type of the arc.‘0’ is the flat bridge, ‘1’ to ‘6’ are six types of arch bridges, and these six tags correspond to the categories in section 1.1.1 |
| material  | The material of the bridge body‘1’ is the wooden bridge, ‘2’ is the stone bridge, ‘3’ is the iron bridge, |
|  railing  | The type of the bridge railings‘2’ is the stone railing, ‘3’ is the metal railing |
|  Comment  |                                                              |

#### Repository Architecture: 

```
├── Bridges_simple.gh: Basic bridge generator script
├── Muti_stairs.gh: Bridge generator with Multi-level stairs
├── round_stair_with_long_edges.gh: Bridge generator with round stairs
├── round_stairs_with_railings.gh: Bridge generator with round stairs and railings in different angles
├── bridges_stairs_angles.gh: Bridge generator with round stairs and railings in different angles
├── bridges_description.json: JSON file contains only text description data
├── bridges_all.json & bridges_all.csv file contains only all data and parameters
├── README.md
├── data: pdf source files and building plans
├── models: output model results of bridges, including obj, 3dm and gh files
├── scripts: python tool scripts
└── others: other model result of our intermediate steps
```

