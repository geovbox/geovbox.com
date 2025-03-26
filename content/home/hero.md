+++
# Hero widget.
widget = "blank"
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 3 # Order that this section will appear.

title = '<i class="fas fa-globe-asia"></i> 构造模拟'
subtitle = ""

# Hero image (optional). Enter filename of an image in the `static/img/` folder.
#hero_media = "ZDEM_logo.png"

[design]
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns = "2"

[design.background]
  # Apply a background color, gradient, or image.
  #   Uncomment (by removing `#`) an option to apply it.
  #   Choose a light or dark text color by setting `text_color_light`.
  #   Any HTML color name or Hex value is valid.

  # Background color.
  color = "#FFF"

  # Background gradient.
  # gradient_start = "#4bb4e3"
  # gradient_end = "#2b94c3"

  # Background image.
  # image = ""  # Name of image in `static/img/`.
  # image_darken = 0.6  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.

  # Text color (true=light or false=dark).
  text_color_light = false

[design.spacing]
  # Customize the section spacing. Order is top, right, bottom, left.
  #padding = ["20px", "0", "20px", "0"]

[advanced]
 # Custom CSS.
 css_style = ""

 # CSS class.
 css_class = ""
+++

{{% row "featurette" %}}
{{% col "col-md-4" %}}

{{< figure src="https://doc.geovbox.com/latest/_images/shearSS.gif" title=""  width="300px" >}}

[一个示例学会构造数值模拟](https://doc.geovbox.com/latest/push/)

{{%/ col %}}
{{% col "col-md-4" %}}

{{< figure src="https://doc.geovbox.com/latest/_images/syn_erosion.gif" title=""  width="400px" >}}

[剥蚀](https://doc.geovbox.com/latest/struct/ex2_syn_erosion/)

{{%/ col %}}

{{% col "col-md-4" %}}

{{< figure src="https://geovbox.com/blog/20201102/normal_fault_synsed.gif" title=""  width="200px" >}}

{{< figure src="https://geovbox.com/blog/20201102/all_0000260000_ini.jpg" title=""  width="200px" >}}

[伸展、生长、断层传播褶皱的离散元模拟(Basin Research)](https://geovbox.com/blog/20201102/)

{{%/ col %}}

{{%/ row %}}


