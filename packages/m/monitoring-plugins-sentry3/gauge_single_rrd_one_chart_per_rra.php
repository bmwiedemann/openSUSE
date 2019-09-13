<?php
#
# Copyright (c) 2006-2010 Joerg Linge (http://www.pnp4nagios.org)
# Plugin: check_icmp [Multigraph]

#
# Define some colors ..
#
define("_WARNRULE", '#FFFF00');
define("_CRITRULE", '#FF0000');
#define("_AREA",     '#EACC00');
define("_AREA",     '#336699');
define("_LINE",     '#CF00FF');

#
# Inital Logic ...
#

foreach ($DS as $i) {

	$warning	= "";
	$critical	= "";

	$minimum	= "";
	$maximum	= "";

	$criticallower	= "";
	$warninglower	= "";

	$lower		= "";
	$upper		= "";

	$vlabel		= "";
	$legend		= "";
	
	if ($WARN[$i] != "") {
		$warning = $WARN[$i];
	}
	if ($WARN_MAX[$i] != "") {
		$warning = $WARN_MAX[$i];
	}
	if ($WARN_MIN[$i] != "") {
		$warninglower = $WARN_MIN[$i];
	}
	if ($CRIT[$i] != "") {
		$critical = $CRIT[$i];
	}
	if ($CRIT_MAX[$i] != "") {
		$critical = $CRIT_MAX[$i];
		$upper = " --upper-limit=" . $CRIT_MAX[$i];
	}
	if ($CRIT_MIN[$i] != "") {
		$criticallower = $CRIT_MIN[$i];
		$lower = " --lower-limit=" . $criticallower;
	}
	if ($MIN[$i] != "") {
		$lower = " --lower-limit=" . $MIN[$i];
		$minimum = $MIN[$i];
	}
	if ($MAX[$i] != "") {
		$upper = " --upper-limit=" . $MAX[$i];
		$maximum = $MAX[$i];
	}
	if ($UNIT[$i] == "%%") {
		$vlabel = "%";
	}
	else {
		$vlabel = $UNIT[$i];
	}

	# Define the legend 
	$legend = $NAME[$i];	

	# Define the generic RRD values
	$opt[$i] = '--vertical-label "' . $vlabel . '" --title "' . $hostname . ' / ' . $servicedesc . '"' . $lower . $upper;

	$def[$i]  = rrd::def("var1", $RRDFILE[$i], $DS[$i], "AVERAGE") ;
        #$def[$i] .= rrd::line1("var1", _LINE) ;
	$def[$i] .= rrd::area("var1", _AREA , $legend . " ") ;
        $def[$i] .= "COMMENT:\"  \\l\" " ;
	$def[$i] .= rrd::gprint("var1", "LAST", "Current %6.2lf $UNIT[$i]") ;
	$def[$i] .= rrd::gprint("var1", "AVERAGE", "Average %6.2lf $UNIT[$i]") ;
	$def[$i] .= rrd::gprint("var1", "MAX", "Maximum %6.2lf $UNIT[$i]\\n") ;

        $def[$i] .= "COMMENT:\"  \\l\" " ;
        $def[$i] .= "COMMENT:\"" . $legend . "\\l\" ";

        if ($warning != "" && ($warning != $critical)) {
                $def[$i] .= rrd::hrule($warning, _WARNRULE , "Warning on    "  . sprintf("%6.2lf",$warning) ." ". $vlabel);
        }
        if ($critical != "") {
                $def[$i] .= rrd::hrule($critical, _CRITRULE ,"Critical on   " . sprintf("%6.2lf",$critical) ." ". $vlabel ."\\j");
        }
        if ($warninglower != "" && ($warninglower != $criticallower)) {
                $def[$i] .= rrd::hrule($warninglower, _WARNRULE ,"Warning on low" . sprintf("%6.2lf",$warninglower) ." ". $vlabel);
        }
        if ($criticallower != "") {
                $def[$i] .= rrd::hrule($criticallower, _CRITRULE ,"Critical on low" . sprintf("%6.2lf",$criticallower) ." ". $vlabel ."\\j");
        }

}

?>
