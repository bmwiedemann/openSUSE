#!/bin/bash
git diff v0.10.1..HEAD -- ':(exclude)Rakefile' > ../suse.patch
