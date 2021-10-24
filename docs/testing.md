# Testing for MS4 <!-- omit in toc -->
The testing oultined below is organised by functionality and or user story.
Note: Testing is ongoing with final changes to the appearance of the site. Some of the screenshots may not match exactly with the submitted version in terms of the appearance.

The format of the sections here is to briefly describe the test actinos taken and give a result.

[Back to README](../README.md)

- [Tests For First-Time or Non-Registered User](#tests-for-first-time-or-non-registered-user)
  - [As a first-time visitor, the purpose and overall content of the site is clear and easy to navigate](#as-a-first-time-visitor-the-purpose-and-overall-content-of-the-site-is-clear-and-easy-to-navigate)
  - [The site appears and trustworthy](#the-site-appears-and-trustworthy)
  - [The calculator feature works](#the-calculator-feature-works)
  - [The sequestration figure and the doughnut reprsentation on the home page update correctly after a donation](#the-sequestration-figure-and-the-doughnut-reprsentation-on-the-home-page-update-correctly-after-a-donation)
  - [Access to site content is limited as non-logged in user, encouraging registration](#access-to-site-content-is-limited-as-non-logged-in-user-encouraging-registration)
- [Donations and Shop Tests](#donations-and-shop-tests)
  - [Test that clicking Donate brings me to the Log In page if not logged in.](#test-that-clicking-donate-brings-me-to-the-log-in-page-if-not-logged-in)
  - [Test that clicking to proceed to Checkout brings me to Log In page if not logged in](#test-that-clicking-to-proceed-to-checkout-brings-me-to-log-in-page-if-not-logged-in)
  - [Test stock information](#test-stock-information)
  - [Test Stock Update in DB](#test-stock-update-in-db)
  - [Verify that the order information together with the payment status is available to a user on their 'My Orders' page](#verify-that-the-order-information-together-with-the-payment-status-is-available-to-a-user-on-their-my-orders-page)
  - [Verify that a receipt is sent to the buyer on successful payment](#verify-that-a-receipt-is-sent-to-the-buyer-on-successful-payment)
- [Project Edits and Updates](#project-edits-and-updates)
  - [Verify that as a normal logged in user, I can only view projects and updates](#verify-that-as-a-normal-logged-in-user-i-can-only-view-projects-and-updates)
  - [Verify that as a designated 'author', I can add or delete project updates and edit project details](#verify-that-as-a-designated-author-i-can-add-or-delete-project-updates-and-edit-project-details)
- [Calculator Page](#calculator-page)
  - [Verify the calculation is working correctly](#verify-the-calculation-is-working-correctly)
  - [Verify that the last column in the table 'As % of your fuel emission' is calculated correctly](#verify-that-the-last-column-in-the-table-as--of-your-fuel-emission-is-calculated-correctly)
  - [Verify that all the buttons work and the page is dynamically loaded based on the user input](#verify-that-all-the-buttons-work-and-the-page-is-dynamically-loaded-based-on-the-user-input)
- [Test Contact Form functionality](#test-contact-form-functionality)
- [Test Cross-Browser](#test-cross-browser)
- [Responsiveness Testing](#responsiveness-testing)

## Tests For First-Time or Non-Registered User

### As a first-time visitor, the purpose and overall content of the site is clear and easy to navigate

Navigate to the site and asses whether the purpose of the site is clearly evident and/or accessible to a non-registered user.

Result: Pass
When I navigate to the site, the image, heading, sub-heading are all consistent.
I can easily access the 'About' page from the landing page and this clearly outlines the site purpose.
I can also easil visit and use the calculator functionality and this illustrates with a meaningful example of how a donation might help to store carbon and offset personal lifetyle emissions.

### The site appears and trustworthy
Steps:
1. Check the Calculator page to assess trustworthiness. It should make it clear that the claims for sequestration/offsets are based on reliable data. Verify that the site does not actively request any payments or card data - in fact the user cannot donate without becoming a registered user.

Result: Pass 
When I navigate to the mentioned pages, resources are mentioned and I can verify that these exist.

### The calculator feature works
 As a non-registered or non-logged-in user, attempt to use the calculator function and check that the sequestration potential per 50 euro donation is calculated based on my input.
   
Result: Pass
The calculator page is accessible and the calculations update in line with my inputs. The 'sequestration potential' table updates dynamically with my input.

### The sequestration figure and the doughnut reprsentation on the home page update correctly after a donation
Check the value of the CO2 sequestration before making a donation. Make a donation, and then refresh the home page to verify the new value has been populated. 

Result: Pass

### Access to site content is limited as non-logged in user, encouraging registration
Verify that certain parts of the site are inaccesible while not logged in.
Non-logged in user can vistit the project pages, the calculator, and the shop. However they cannot make a donation, buy something, or access their profile (My Orders) without being logged in.

Result: Pass.

## Donations and Shop Tests

### Test that clicking Donate brings me to the Log In page if not logged in.
Result: Pass

### Test that clicking to proceed to Checkout brings me to Log In page if not logged in
Result: Pass
A non-logged in user can add items to their cart and browse products but they cannot go to checkout without first logging in.

### Test stock information
As admin, check the stock for a particular product in the Django admin.
Verify that this is correctly reflected on the product page.
To allow for some leeeway in terms of variety and any damage that might occur to trees at a nursery, verify that a buffer of 5 trees is always maintained - ie , a purchase cannot reduce the stock level below 5. User is informed of the max number available.
Result: pass

### Test Stock Update in DB
As an admin, check the stock for a particular product in the Django Admin.
Proceed to site and make a purchase of the product * 2. 
Return to admin and verify that the stock level has updated and is also correctly reflected in the UI for the next buyer.
Result: Pass

### Verify that the order information together with the payment status is available to a user on their 'My Orders' page
As a user, make a purchase of an item and verify that the order details are visible on the My Orders page when payment has gone through.

Result: Pass

### Verify that a receipt is sent to the buyer on successful payment
Stripe does not send email receipts in test mode. However, on the stripe dashboard a receipt can be triggered for a particular stripe payment (as would occur out of test mode). To verify that once out of test mode the receipt functionality would work:
Make a payment as a logged in user.
Check the order number.
In the Django Admin, find the corresponding Stripe payment ID.
On the Stripe dashboard, locate the order and trigger an email receipt. 
Verify that the email is received, for the correct amount, at the email address given for the logged in user.

![Send receipt for paid order](/docs/readme_images/resolve_payment_order.png)

Result: Pass

## Project Edits and Updates
### Verify that as a normal logged in user, I can only view projects and updates
Log in as a normal user and view project pages and updates.
Verify that no option is displayed to add an update or edit project details
Result: Pass

### Verify that as a designated 'author', I can add or delete project updates and edit project details
Log in as a user assigned 'author' stats for a projetc.
Verify that I now see the option to edit the project details or to add an update for the project. (Note: Updates only have add or delte options, but no edit functionality.)
Result: Pass

## Calculator Page
### Verify the calculation is working correctly
Make an entry at for fuel cost and type and press the button to estimate emissions.
Double-check the result against an expected result calculated offline.
Result: Pass

### Verify that the last column in the table 'As % of your fuel emission' is calculated correctly
As above, double-check against values calculated offline.
Result: Pass

### Verify that all the buttons work and the page is dynamically loaded based on the user input
Result: Pass

## Test Contact Form functionality
Verify that the contact form works by filling out a valid entry and submitting. Verify that the email is received by 'ms4.citizentree@gmail.com' and the email provided by the peson submitting the form.

Result: Pass

## Test Cross-Browser
The site was developed and all primary tests were conducted using a laptop and monitor.

With this setup, the site was tested in the following browsers:
* Chrome
* Firefox
* Safari
* Opera

In general, no major hiccups were found but here were some discrepancies. For example, the home page showing the doughnut chart displays as intended in Chrome, Safari, and Opera, but Firefox displays it in a larger size. This is a display issue and not critical and I have run out of time to do further testing so have left any remaining display issues as they are. As far as I have tested, the functionality works as intended in all major browsers. 

Result: Pass with issues for investigation

## Responsiveness Testing
To check responsiveness, the site has been checked using:
* The Inspect option in Google Chrome simulating different device widths
* An Android phone 
* An iPhone
* An Android tablet
* An iPad

I also attempted to test with some online responsiveness checkers but found this to be a problem due to X-Frame-Options.
The [Django documentation](https://docs.djangoproject.com/en/3.2/ref/clickjacking/) says: "By default, the middleware will set the X-Frame-Options header to DENY for every outgoing HttpResponse. If you want any other value for this header instead, set the X_FRAME_OPTIONS setting".
I have not maintained any other setting and have left the default in place:
![X-Frame-Options](/docs/readme_images/middleware_xframe.png)

The upshot is that tools like [Am I Responsive](https://responsivedesign.is/articles/xframe-options/) cannot access the site.

One tool I could use was Chrome's Lighthouse. Results here also have room for improvement:
![Example Lighthouse Report - Calculator page](/docs/readme_images/lighthouse_report.png)

Result:
In general, the site maintains it usability but there are areas for improvement:
* On the calculator page, the FAQs can appear outside (below) the viewport but the focus does not switch, so the user has to scroll down to see the output. A user could mistakenly think that nothing has been returned and not realize they need to scroll. To be fixed (not done before submission).
* When accessing the cart, the table is wider than the view port so the user has to scroll horizontally. Depending on the device, this can result in the header and footer not populating the full width of the page. To be fixed (not done before submission).

Overall: Pass with some issues for further investigation