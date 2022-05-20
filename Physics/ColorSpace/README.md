# Color Space

## Mechanism

### visible spectrum
Human eyes have two kinds of light sensitive cells, rod cell and cone cell.  
Cone cell can detect light in the visible spectrum.  
But human only have three types of cone cell, which are red, green, blue.  
Thus, when there are lots of lights combined with different wavelength, human brain will interpolate the color between red and blue.  
However, if a wavelength of a light is combined with red and blue, the problem is that the color should not be green.  
To deal with this problem, human brain create Magenta.

Reference: [这个世界上根本不存在紫色！ ( 眼见为识)](https://www.youtube.com/watch?v=vv79wigS-4I)

Rod cell is sensitive to luminance.  
When there is dark, rod cell can see boundary of objects.

### sensitivity
Green > Red > Blue
<img src="https://qph.cf2.quoracdn.net/main-qimg-de71b9bcbb3a8503ea1b8c968a9f2b29" Height="480" />


## CIE space
CIE (International Commission on Illumination) is human color vision.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/CIE1931xy_gamut_comparison.svg/800px-CIE1931xy_gamut_comparison.svg.png" Height="480" />

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Colorspace.png/220px-Colorspace.png" Height="480" />


### YUV space

Due to rod cell, human eye is more sensitive at grayscale.  
Thus, in traditional camera space will try to seprate gray and other color.  
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Barn-yuv.png/200px-Barn-yuv.png" />

RGB and YUV is able to calculate by martix.

0:299 0:587 0:114
􀀀0:299 􀀀0:587 0:886
0:701 􀀀0:587 􀀀0:114
###
