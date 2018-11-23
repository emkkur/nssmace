/*global $ */
$("document").ready(function () {
	"use strict";
	$(".box").animate({
		top: "0px"
	}, 0, function () {
		$(".box").animate({
			width: "400px"
		}, 0, function () {
			$(".box").animate({
				height: "460px"
			}, 0, function () {
				$(".box").animate({
					borderRadius: "10px"
				}, 0, function () {
					$("img").fadeIn(0, function () {
						$("h3").slideDown(0, function () {
							$(".form-control").slideDown(0, function () {
								$(".checkbox").show(0, function () {
									$(".checkbox").animate({left: "0px"}, 0, function () {
										$(".btn-primary").slideDown(0, function () {
											$("a").fadeIn(function () {
												$("a").animate({
													right: "0px"
												}, 0);
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