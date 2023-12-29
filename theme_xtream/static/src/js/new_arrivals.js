odoo.define('theme_xtream.new_arrivals', function(require){
'use strict';

var Animation = require('website.content.snippets.animation');

var ajax = require('web.ajax');

Animation.registry.arrival_product = Animation.Class.extend({
    selector : '.arrivals',
    start: function(){
        var self = this;
        ajax.jsonRpc('/get_arrival_product', 'call', {})
        .then(function (data) {
            if(data){
                self.$target.empty().append(data);
            }
        });
    }
    });
Animation.registry.jobs_snippet = Animation.Class.extend({
    selector : '.fetch_jobs',
    start: function(){
        var self = this;
        ajax.jsonRpc('/get_random_jobs', 'call', {})
        .then(function (data) {
            if(data){
                self.$target.empty().append(data);
            }
        });
    }
    });

Animation.registry.bitcoin_snippet = Animation.Class.extend({
    selector : '.bitcoin',
    start: function(){

     var self = this;
            ajax.jsonRpc('/get_bitcoin_price', 'call', {})
            .then(function (data) {
                if(data){
                    var data = [
                        ["2013", 10000],
                        ["2014", 20000],
                        ["2015", 4000],
                        ["2016", 5000],
                        ["2017", 6000],
                        ["2018", 7000],
                        ["2019", data['price']],
                    ];
                    var dataSet = anychart.data.set(data);
                    var firstSeriesData = dataSet.mapAs({x: 0, value: 1});
                    var chart = anychart.line();
                    var firstSeries = chart.line(firstSeriesData);
                    firstSeries.name("Roger Federer");
                     chart.legend().enabled(true);
                     chart.title("Bitcoin Price");

  // specify where to display the chart
                     chart.container("container");

  // draw the resulting chart
                    chart.draw();

                }
            });


  // create a data set


  // map the data for all series


  // create the series and name them


////        ajax.jsonRpc('/get_random_jobs', 'call', {})
////        .then(function (data) {
////            if(data){
////                self.$target.empty().append(data);
////            }
////        });
    }
    });
});