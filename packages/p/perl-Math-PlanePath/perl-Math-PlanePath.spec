#
# spec file for package perl-Math-PlanePath
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-Math-PlanePath
Version:        128
Release:        0
#Upstream: GPL-1.0-or-later
%define cpan_name Math-PlanePath
Summary:        Points on a path through the 2-D plane
License:        GPL-3.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Math::Libm)
BuildRequires:  perl(constant::defer) >= 5
Requires:       perl(Math::Libm)
Requires:       perl(constant::defer) >= 5
%{perl_requires}

%description
This is a base class for some mathematical paths which map an integer
position '$n' to and from coordinates '$x,$y' in the 2D plane.

The current classes include the following. The intention is that any
'Math::PlanePath::Something' is a PlanePath, and supporting base classes or
related things are further down like 'Math::PlanePath::Base::Xyzzy'.

    SquareSpiral           four-sided spiral
    PyramidSpiral          square base pyramid
    TriangleSpiral         equilateral triangle spiral
    TriangleSpiralSkewed   equilateral skewed for compactness
    DiamondSpiral          four-sided spiral, looping faster
    PentSpiral             five-sided spiral
    PentSpiralSkewed       five-sided spiral, compact
    HexSpiral              six-sided spiral
    HexSpiralSkewed        six-sided spiral skewed for compactness
    HeptSpiralSkewed       seven-sided spiral, compact
    AnvilSpiral            anvil shape
    OctagramSpiral         eight pointed star
    KnightSpiral           an infinite knight's tour
    CretanLabyrinth        7-circuit extended infinitely

    SquareArms             four-arm square spiral
    DiamondArms            four-arm diamond spiral
    AztecDiamondRings      four-sided rings
    HexArms                six-arm hexagonal spiral
    GreekKeySpiral         square spiral with Greek key motif
    MPeaks                 "M" shape layers

    SacksSpiral            quadratic on an Archimedean spiral
    VogelFloret            seeds in a sunflower
    TheodorusSpiral        unit steps at right angles
    ArchimedeanChords      unit chords on an Archimedean spiral
    MultipleRings          concentric circles
    PixelRings             concentric rings of midpoint pixels
    FilledRings            concentric rings of pixels
    Hypot                  points by distance
    HypotOctant            first octant points by distance
    TriangularHypot        points by triangular distance
    PythagoreanTree        X^2+Y^2=Z^2 by trees

    PeanoCurve             3x3 self-similar quadrant
    PeanoDiagonals         across unit squares
    WunderlichSerpentine   transpose parts of PeanoCurve
    HilbertCurve           2x2 self-similar quadrant
    HilbertSides           along sides of unit squares
    HilbertSpiral          2x2 self-similar whole-plane
    ZOrderCurve            replicating Z shapes
    GrayCode               Gray code splits
    WunderlichMeander      3x3 "R" pattern quadrant
    BetaOmega              2x2 self-similar half-plane
    AR2W2Curve             2x2 self-similar of four parts
    KochelCurve            3x3 self-similar of two parts
    DekkingCurve           5x5 self-similar, edges
    DekkingCentres         5x5 self-similar, centres
    CincoCurve             5x5 self-similar

    ImaginaryBase          replicate in four directions
    ImaginaryHalf          half-plane replicate three directions
    CubicBase              replicate in three directions
    SquareReplicate        3x3 replicating squares
    CornerReplicate        2x2 replicating "U"
    LTiling                self-similar L shapes
    DigitGroups            digits grouped by zeros
    FibonacciWordFractal   turns by Fibonacci word bits

    Flowsnake              self-similar hexagonal tile traversal
    FlowsnakeCentres         likewise but centres of hexagons
    GosperReplicate        self-similar hexagonal tiling
    GosperIslands          concentric island rings
    GosperSide             single side or radial

    QuintetCurve           self-similar "+" traversal
    QuintetCentres           likewise but centres of squares
    QuintetReplicate       self-similar "+" tiling

    DragonCurve            paper folding
    DragonRounded          paper folding rounded corners
    DragonMidpoint         paper folding segment midpoints
    AlternatePaper         alternating direction folding
    AlternatePaperMidpoint alternating direction folding, midpoints
    TerdragonCurve         ternary dragon
    TerdragonRounded       ternary dragon rounded corners
    TerdragonMidpoint      ternary dragon segment midpoints
    AlternateTerdragon     alternate ternary dragon
    R5DragonCurve          radix-5 dragon curve
    R5DragonMidpoint       radix-5 dragon curve midpoints
    CCurve                 "C" curve
    ComplexPlus            base i+realpart
    ComplexMinus           base i-realpart, including twindragon
    ComplexRevolving       revolving base i+1

    SierpinskiCurve        self-similar right-triangles
    SierpinskiCurveStair   self-similar right-triangles, stair-step
    HIndexing              self-similar right-triangles, squared up

    KochCurve              replicating triangular notches
    KochPeaks              two replicating notches
    KochSnowflakes         concentric notched 3-sided rings
    KochSquareflakes       concentric notched 4-sided rings
    QuadricCurve           eight segment zig-zag
    QuadricIslands           rings of those zig-zags
    SierpinskiTriangle     self-similar triangle by rows
    SierpinskiArrowhead    self-similar triangle connectedly
    SierpinskiArrowheadCentres  likewise but centres of triangles

    Rows                   fixed-width rows
    Columns                fixed-height columns
    Diagonals              diagonals between X and Y axes
    DiagonalsAlternating   diagonals Y to X and back again
    DiagonalsOctant        diagonals between Y axis and X=Y centre
    Staircase              stairs down from the Y to X axes
    StaircaseAlternating   stairs Y to X and back again
    Corner                 expanding stripes around a corner
    PyramidRows            expanding stacked rows pyramid
    PyramidSides           along the sides of a 45-degree pyramid
    CellularRule           cellular automaton by rule number
    CellularRule54         cellular automaton rows pattern
    CellularRule57         cellular automaton (rule 99 mirror too)
    CellularRule190        cellular automaton (rule 246 mirror too)
    UlamWarburton          cellular automaton diamonds
    UlamWarburtonQuarter   cellular automaton quarter-plane

    DiagonalRationals      rationals X/Y by diagonals
    FactorRationals        rationals X/Y by prime factorization
    GcdRationals           rationals X/Y by rows with GCD integer
    RationalsTree          rationals X/Y by tree
    FractionsTree          fractions 0<X/Y<1 by tree
    ChanTree               rationals X/Y multi-child tree
    CfracDigits            continued fraction 0<X/Y<1 by digits
    CoprimeColumns         coprime X,Y
    DivisibleColumns       X divisible by Y
    WythoffArray           Fibonacci recurrences
    WythoffPreliminaryTriangle
    PowerArray             powers in rows
    File                   points from a disk file

And in the separate Math-PlanePath-Toothpick distribution

    ToothpickTree          pattern of toothpicks
    ToothpickReplicate     same by replication rather than tree
    ToothpickUpist         toothpicks only growing upwards
    ToothpickSpiral        toothpicks around the origin

    LCornerTree            L-shape corner growth
    LCornerReplicate       same by replication rather than tree
    OneOfEight
    HTree                  H shapes replicated

The paths are object oriented to allow parameters, though many have none.
See 'examples/numbers.pl' in the Math-PlanePath sources for a sample
printout of numbers from selected paths or all paths.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples
%license COPYING

%changelog
