
// Loosely based on Carbon Emission Calculator by Matt Bond: https://codepen.io/matt-bond/pen/ROrbOX

let gCO2PerL_P = 2.3; // Kg of CO2 released by combustion of 1 litre (Petrol)
let gCO2PerL_D = 2.6; // Kg of CO2 released by combustion of 1 litre (Diesel)
let costPL_P = 1.43; // Cost of petrol per litre (AA)
let costPL_D = 1.34; // Cost of diesel per litre (AA)
let natWoodlandArea;
let woodPastureArea;
let hedgeArea;
let co2PerYear;


// Calculate and present the CO2 footprint of user's fuel use
function fuelFootprint() {
    let litresPerWeek; // Calculated - weekly spend divided by cost per litre 
    let co2PerWeek;    // Calculated - litres per week by CO2 per litre 
    let co2PerLitre;   // Value is determined based on whether user selects petrol or diesel 
    let weeklySpend = document.getElementById("week_spend").value; // Get user's weekly fuel spend from UI

    // Get the fuel type source (get value from radio button). Resource:https://www.youtube.com/watch?v=cSuEAD-Tnd4
    let fuel = document.querySelector('input[name="fuel_type"]:checked').value
    
    // Calculate litres per week and assign emission value
    if (fuel == 'diesel'){
            litresPerWeek = weeklySpend/costPL_D;
            co2PerLitre = gCO2PerL_D; 
        }
    else {
            litresPerWeek = weeklySpend/costPL_P;
            co2PerLitre = gCO2PerL_P;
        }

    // Calculate CO2 emissions per week for transport fuel
    co2PerWeek = parseInt(litresPerWeek*co2PerLitre);
    co2PerYear = 52*co2PerWeek;
    
    //Populate result to page    
    document.getElementById("emission-results").innerHTML =`
    <div class='container text-center'>
              <h2 class='jumbo-header-neutral'>Your weekly emission of CO2 from driving is: ${co2PerWeek} Kg</h2>
            <br/>
              <h2 class='jumbo-header-neutral'>Your annual emission of CO2 from driving is: ${co2PerYear} Kg</h2>
            <br/>
            <button class='btn-success rounded-sm mb-3' onclick='offsetPotential()'>Help Me to Offset This</button>
          </div>
          `
    // Move to bottom of div so user doesn't have to scroll to see result on small screen - https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView
    emissionsView = document.getElementById("emission-results");      
    emissionsView.scrollIntoView(alignToTop=false);     
    // In case a user changes the calc values afterwards, clear the existing offset/estimate divs   
    document.getElementById("offset-potential").innerHTML = `` 
    document.getElementById("tell-estimate").innerHTML = ``        
}

// Calculate and present the offset potential of a donation to Citizen Tree in the context of the user's emissions

function offsetPotential(){
    // Values for table (As % of your Fuel Emission)
    natWoodlandArea = (7330/co2PerYear).toFixed(3);
    woodPastureArea = (4800/co2PerYear).toFixed(3);
    hedgeArea = (3600/co2PerYear).toFixed;

    document.getElementById("offset-potential").innerHTML =`
    <div class="jumbotron bg-cover text-white offset">
<!-- Source of opacity styling for bg image: https://codepen.io/JacobLett/pen/vPQKWd -->
<h1 class ="jumbo-header-neutral">Sequestration Potential with Citizen Tree</h1>
<p class="jumbotron-para-reg">
  The idea of the fuel emissions is just you give some perspective, not to beat you over the head with a green stick. 
  We all need to get around and transport options are limited.</p>

  <p>So, what can you do and how can we help?</p>

  <p>There are tons of online resources about how to live a less carbon-intense lifestyle. No doubt you can find some options suitable for your own situation.
  Our focus is a little different - we help partner landowners and other interested parties to manage land in a way that promotes carbon sequestration. 
  Sometimes, trees are not the best option (and could result in existing land switching from being a C sink to a C source).
  We also promotoe awareness and action among participating groups (schools, community organisations, farmers) about climate change and biodiverstiy loss. 
  We help foster practical skills among young people and an appreciation for the timescales on which all this happens. 
  To paraphrase a book title of a few years ago, we're trying to work fast and slow.
  We promote a low-input, minimal disturbance work pattern and where something is not broken we don't propose to fix it with a tree, much as we love them.</p>
  
  <p>For the potential of using trees in an Irish context, we're basing this introductory content on a recent meta-study by Penny Anderson (BSc., MSc., CEcol, FCIEEM, Ecologist). 
  Relevant to what we do are the following figures:</p>
  
  <div class="table-responsive">
    <table class="table table-dark">
      <caption>Sequestration Potential of Different Management Approaches</caption>
  <thead>
    <tr>
      <th scope="col">Sequestration Approach</th>
      <th scope="col">Annual (estimate) Kg/ha</th>
      <th scope="col">Area Contribution per 50 eu Donation (% of Ha.)</th>
      <th scope="col">As % of Your Fuel Emission</th>

    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Natural woodland generation on former arable soils</th>
      <td>7.33-14.3 tCO2ha/yr over c.120 yrs</td>
      <td>20 trees or 1% of a Ha.</td>
      <td>${natWoodlandArea}</td>
    </tr>
    <tr>
      <th scope="row">Create wood pasture from pasture</th>
      <td>4.8-5.7 (@ 10% tree cover)</td>
      <td>20 trees or 10% of a Ha.</td>
      <td>${woodPastureArea}</td>
    </tr>
    <tr>
      <th scope="row">Hedge restoration/adding trees</th>
      <td>3.67-5.87 1-1.6</td>
      <td>20 trees (% varies widely)</td>
      <td>N/A</td>
    </tr>
  </tbody>
    </table>
    <br>
    <div class="text-center">
    <button class='btn-success rounded-sm mb-3 text-center' onclick='tellEstimate()'>How is this Calculated?</button>
    </div>
  </div>
    `
    let offsetView = document.getElementById("offset-potential");
    offsetView.scrollIntoView(alignToTop=true); // https://www.w3schools.com/jsref/met_element_scrollintoview.asp
}


function tellEstimate(){
  let estimateView = document.getElementById("tell-estimate");
  document.getElementById("tell-estimate").innerHTML =`
  <div class="jumbotron bg-cover text-white estimate">
<!-- Source of opacity styling for bg image: https://codepen.io/JacobLett/pen/vPQKWd -->
<h1 class ="jumbo-header-neutral">How do we come up with our estimate?</h1>
<p class="jumbotron-para-reg">
  At Citizen Tree, we have currently have 3 contribution options for individuals - 20, 50, 100.</p>

  <p>Anything you contribute makes a big difference. However, it's not always a straight line from a contribution to a tree or a wood pasture sequestering carbon.</p>

  <p>All money from donations is spread across our various projects on an as-needed basis. The uses it might be put to include:</p>
  <ul>
    <li>Buy materials for a raised bed at a school in which to grow locally-collected acorns</li>
    <li>Buy tree guards (against hare damage) for young trees planted into an particpating landowner's field</li>
    <li>Buy tools - spades, secateurs, markers etc</li>
    <li>The list goes on....</li>
</ul>
  
  <p>All of the money raised get's used directly in Citizen Tree projects. Volunteers do not get paid, landowners do not get compensated.</p>
  
  <p>We sat down and, taking all the above into account, came up with an estimate that a 50 euro contribution could usefully be thought of as a contribution of approximately 20 trees.  
    Given a planting density of approximately 2000 per hectare on new sites, this converts to 1% of a hectare.</p>
  <p>Using the figures provided in the previous table, we then calculate the corresponding percentage of the sequestration potential per hectare estimated for various management approaches.</p>
  <p>For example, for woodland establishment, this is (at the lower estimate range) about 7330Kg per hectare per year. 1% of that is 73Kg. Therefore, in the context of a woodland project, a 50 euro contribution equates to facilitating an annual CO2 sequestration of 73Kg.</p>
    <br>
  <p>We don't take accepting money from the public lightly. All contributors receive a quarterly update on our activities and plans. You are also welcome to join our workdays.
    Depending on the scale of the project and the arrangement with landowners, some planted woodlands are also open to Citizen Tree members (this is not always the case, please chaeck with us).
    <br>
    <br>
    <div class="text-center">
    <button class='btn-success rounded-sm mb-3 text-center' onclick='tellCertificate()'>Do I get a certificate?</button>
    <button class='btn-success rounded-sm mb-3 text-center' onclick='tellCorporate()'>Do you have corporate support options?</button>
    <button class='btn-success rounded-sm mb-3 text-center' onclick='tellOwnership()'>Who owns the planted trees?</button>
    <button class='btn-success rounded-sm mb-3 text-center' onclick='tellSpecificProject()'>Can I sponsor a specific project?</button>
    <button class='btn-success rounded-sm mb-3 text-center' onclick='tellSpecificProject()'>As a landowner, how do I get involved?</button>
    </div>
    <div id="query_answer"></div>
  </div>
  `
  estimateView.scrollIntoView(alignToTop=true);
}

