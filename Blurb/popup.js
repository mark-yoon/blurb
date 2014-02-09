// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

/**
 * Global variable containing the query we'd like to pass to Flickr. In this
 * case, kittens!
 *
 * @type {string}
 */


//This function shows an example of how we're changing it
 function myFunction() {
  x=document.getElementById("l1");  // Find the element
  x.innerHTML="Changed!";
  x.href="https://www.google.com";   // Change the content
}      

//This function will is the actually one we will use
// function myFunction(id, artname, url) {
//  x=document.getElementById(id);  // Find the element
//  x.innerHTML=artname;
//  x.href=url;   // Change the content
//}      

document.addEventListener('DOMContentLoaded', function() {
    var link = document.getElementById('button');
    // onClick's logic below:
    link.addEventListener('click', function() {
 	
      $.getJSON('localhost:8080', function(data) {
 	  alert("test2");
 	  });
    });
});
