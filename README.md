# Predicting Surface Roughness of Additive manufactured products with Machine Learning.
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)


3D printing or Additive Manufacturing is a promising digital manufacturing technique that produces 
parts layer by layer. Although 3D printing technology has different methods, 
the fused deposition method (FDM) is the most extensively used. In FDM, 
generally, Acrylonitrile Butadiene Styrene (ABS), Polylactic acid (PLA) in the 
form of filaments is used to fabricate 3D geometry stacking individual layers. 
In reality, FDM is a complex process with numerous parameters which affect 
the printing quality. The parameters like infill pattern, infill density, nozzle 
temperature, wall thickness, and layer height affect the printing quality of the 
printed material. This work is done to determine the surface roughness of the 
3D printed parts of ABS, PLA materials using Machine Learning.

## __Build Parameters:__

### __Wall thickness__
 For any part wall thickness is the minimum thickness of each 
layer laid by the printer. It is important to choose the value based on the 
material to get an undisturbed, structurally stable product. For every material 
there is a certain value for wall thickness below it is not recommended 
because the material layer cannot be adhesive properly or even it can break 
down under its weight and the required product cannot be formed. Through 
various studies, minimum wall thickness for ABS and PLA material is 
recommended as 1mm and 1.5 mm.

### __Layer Height__

The height of each layer is called layer height or layer thickness. It is one of the 
factors to create good strength of the object. It also affects the printing speed. If 
the layer height is high then the printing speed increases and object can be
created in less time and the object can be created in less time and vice versa, 
but the high layer thickness results in poor mechanical properties of the object 
as there will be no proper adhesion and also gets distorted because of its weight. 
Optimum layer thickness should be chosen to get objects with good surface and 
mechanical properties.

### __Infill Density__

It 
tells about how much material has been laid inside the shell. if the material is
high then it has a high infill density. If the infill density increases then the 
strength of the object increases. Generally, a high infill density object takes 
more time to print. Mostly infill density for sample models 20% of infill density 
is used. Infill density is given in percentages i.e from 0% to 100% means hollow 
objects to solid objects. From various studies the recommended densities for 
various purposes are 
1. standard objects 15% - 50%
2. functional objects 50% - 100%
3. Flexible objects 1% -100%

### __Infill pattern__

It is the pattern that is filled inside the shell. There are 
different types of infill patterns from simple to complex geometries. Infill pattern 
also plays an important role in getting good mechanical properties off the object. 
Different patterns included the line, honeycomb, octet, gyroid, concentric.

[Dataset Courtesy:Kaggle](https://www.kaggle.com/datasets/afumetto/3dprinter?resource=download&select=data.csv)
