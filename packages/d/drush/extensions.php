<?php

$extensions = [];
parse_info('self', $extensions);

exec('composer info -N', $packages);
foreach ($packages as $package) {
  parse_info($package, $extensions);
}

function parse_info($package, &$extensions) {
  if ($package == 'self') {
    exec('composer info -s', $info);
  }
  else {
    exec('composer info ' . escapeshellarg($package), $info);
  }

  $heading = false;
  foreach ($info as $line) {
    if ($line == 'requires' || $line == 'suggests') {
      $heading = $line;
      continue;
    }

    if (!$heading) continue;
    if ($line == '') {
      $heading = false;
      continue;
    }

    if (strpos($line, 'ext-') === 0 || strpos($line, 'php ') === 0)
      $extensions[$heading][] = $line;
  }
}

foreach ($extensions as $type => &$list) {
  sort($list);
}

print_r($extensions);
