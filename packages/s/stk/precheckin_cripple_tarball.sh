# The following source parts of stk may not be distributed for legal
# reasons (bnc#760936)
# Thus we have to cripple the source tree in a way that it still builds.

# Find source tarball + unpack
tmp="$(mktemp)"
trap 'rm -f $tmp; echo 1>&2 "$0 failed"' EXIT
tarsource="$(echo stk-*[0-9].tar.gz)"
if [ ! -s "$tarsource" ] ; then
  echo "Error: cannot find source tarball"
  exit 1
fi
tarbase="${tarsource%.tar.gz}"
tardest="$tarbase-crippled.tar.gz"

rm -rf stk-*-crippled.tar.gz

# Cripple source
echo 1>&2 "Crippling..."

files=$(tar -tf ${tarsource} | grep \
-e /doc/html/classRtMidi.html \
-e /doc/html/classstk_1_1Mandolin.html \
-e /doc/html/classstk_1_1Plucked.html \
-e /doc/html/classstk_1_1Sitar.html \
-e /include/BeeThree.h \
-e /include/BlowHole.h \
-e /include/Bowed.h \
-e /include/Brass.h \
-e /include/Clarinet.h \
-e /include/FM.h \
-e /include/FMVoices.h \
-e /include/Flute.h \
-e /include/HevyMetl.h \
-e /include/Mandolin.h \
-e /include/Mesh2D.h \
-e /include/PercFlut.h \
-e /include/Plucked.h \
-e /include/Rhodey.h \
-e /include/Saxofony.h \
-e /include/Sitar.h \
-e /include/StifKarp.h \
-e /include/TubeBell.h \
-e /include/Twang.h \
-e /include/Wurley.h \
-e /projects/ragamatic/Drone.cpp \
-e /projects/ragamatic/Drone.h \
-e /src/BeeThree.cpp \
-e /src/BlowHole.cpp \
-e /src/Bowed.cpp \
-e /src/Brass.cpp \
-e /src/Clarinet.cpp \
-e /src/FM.cpp \
-e /src/FMVoices.cpp \
-e /src/Flute.cpp \
-e /src/Guitar.cpp \
-e /src/HevyMetl.cpp \
-e /src/Mandolin.cpp \
-e /src/Mesh2D.cpp \
-e /src/PercFlut.cpp \
-e /src/Plucked.cpp \
-e /src/Plucked.cpp \
-e /src/Rhodey.cpp \
-e /src/Saxofony.cpp \
-e /src/Sitar.cpp \
-e /src/StifKarp.cpp \
-e /src/TubeBell.cpp \
-e /src/Twang.cpp \
-e /src/Wurley.cpp \
-e /src/include/soundcard.h)

gzip -cd ${tarsource} > ${tmp}
tar --delete --file=${tmp} ${files}
gzip -c ${tmp} > ${tardest}

echo 1>&2 ""
echo 1>&2 "Successfully crippled tarball. :-("
echo 1>&2 ""

rm -rf $tmp
trap - EXIT
exit 0
