# WA-Real-Estate-Data-Analysis

## Introduction

This project aims to analyze real estate data in Washington state to provide insights into property values. I've used 
Scraping to get the Data from Realtor.com, and then cleaned and imported the data into a SQL database.
Then performed some Exploratory Data Analysis to get some insights into the data. The results are also visualized using Tableau.

## Data Sources

The data for this analysis is sourced from the web scraping of Realtor.com, with the help of the HomeHarvest library linked below:

- [Real Estate Data](https://github.com/Bunsly/HomeHarvest)

Note: I changed the script to get all the zipcodes in WA state. I've added the modified script to this repo.

## Visualization
- [Tableau Dashboard](https://public.tableau.com/views/WAStateRealEstateAnalysisOct_2024/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
<div class='tableauPlaceholder' id='viz1729900027313' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;WA&#47;WAStateRealEstateAnalysisOct_2024&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='WAStateRealEstateAnalysisOct_2024&#47;Dashboard1' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;WA&#47;WAStateRealEstateAnalysisOct_2024&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1729900027313');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='1200px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>