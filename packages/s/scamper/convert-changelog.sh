#!/bin/bash

sed 's/^/  * /' | sed 's/\* \*/ /' | sed 's/\*   /  /' | sed '/^  \* $/d'
