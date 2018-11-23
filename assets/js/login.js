/*global $ */
$("document").ready(function () {
	"use strict";
	$(".box").animate({
		top: "0px"
	}, 1000, function () {
		$(".box").animate({
			width: "400px"
		}, 1000, function () {
			$(".box").animate({
				height: "460px"
			}, 1000, function () {
				$(".box").animate({
					borderRadius: "10px"
				}, 1000, function () {
					$("img").fadeIn(1000, function () {
						$("h3").slideDown(1000, function () {
							$(".form-control").slideDown(1000, function () {
								$(".checkbox").show(700, function () {
									$(".checkbox").animate({left: "0px"}, 1000, function () {
										$(".btn-primary").slideDown(1000, function () {
											$("a").fadeIn(function () {
												$("a").animate({
													right: "0px"
												}, 1000);
											});
										});
									});
								});
							});
						});
					});
				});
			});
		});
	});
});