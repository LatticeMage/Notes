# Project Management


<div class="slide">

## Development Process Management
* Development Framework
    * [[2023 TGDF] 極度邊緣的開發方式 (黃仕成) ](https://youtu.be/yV0aYkDtqp8)
    * [Slides](https://docs.google.com/presentation/d/1SEad3fuaRG9u78X5sLWwab71ZKbSmEBYQwj0Sv2SYAY/edit)
* Task Management Systems
    * Asana, Monday, .....
    * [GitHub Organization](https://github.com/orgs/)
* Document Management Systems
    * Google Doc, .....
    * Github

</div>

<div class="slide">

## Architecture Design
* Setting Plans and Goals
* Documentation

<img src="Trapezoid.svg" width="250">
<img src="Circles.svg" width="250">

</div>


<div class="slide">

## One-Page Presentation

* <button class="download" id="proposal-html" data-url="proposal.html">Download Proposal Template</button>
* <button class="download" id="proposal-yml" data-url="proposal.yml">Download Proposal YML</button>
* [Proposal Converter Tool](https://shinra.posetmage.com/GameDesign/Tool/Converter.html)

* <button class="download" id="business-model-html" data-url="business_model.html">Download Business Model Template</button>
* <button class="download" id="business-model-yml" data-url="business_model.yml">Download Business Model YML</button>

</div>


<div class="slide">

## Risk Management
* Risk Identification
* Risk Mitigation
* Monitoring and Review
  * Align Design Pillars

</div>


<div class="slide">

## Financial Management
* Funding Strategy
* Budget Planning
* Cash Flow Management
* Cost, Salary

</div>


<div class="slide">

## Agile Development

* MVP
  * ![](MVP.webp)
* Spiral Model
  * ![](https://www.bdtask.com/blog/assets/plugins/ckfinder/core/connector/php/uploads/images/xwhat,P20is,P20spiral,P20model,P20for,P20software,P20development.jpg.pagespeed.ic.vL7MBvEhah.webp)
* Vertical Slicing
  * ![](https://upload.wikimedia.org/wikipedia/commons/d/d3/Vertical_slice.png)

</div>


<div class="slide">

## Startup
* action more than plan
* deep observe how user use product
* high frequency feedback 
* (modify One-Page Presentation)



</div>




<script>
document.addEventListener('DOMContentLoaded', function() {
    // Function to handle the download
    function handleDownload(event) {
        const url = event.target.getAttribute('data-url');
        if (url) {
            const link = document.createElement('a');
            link.href = url;
            link.download = ''; // Setting download attribute will trigger the save dialog
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
    }

    // Get all buttons with the class 'download' and add event listeners
    const downloadButtons = document.querySelectorAll('.download');
    downloadButtons.forEach(function(button) {
        button.addEventListener('click', handleDownload);
    });
});

</script>