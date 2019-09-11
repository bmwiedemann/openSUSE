#
# spec file for package FlightGear-data
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define main_version 2018.3
Name:           FlightGear-data
Version:        %{main_version}.4
Release:        0
Summary:        FlightGear base scenery and data files
License:        GPL-2.0-only
Group:          Amusements/Games/3D/Simulation
Url:            http://www.flightgear.org/
Source0:        https://downloads.sourceforge.net/project/flightgear/release-%{main_version}/FlightGear-%{version}-data.tar.bz2
# Remove warnings about hidden files to make other rpmlint warnings readable.
Source1:        FlightGear-data-rpmlintrc
NoSource:       0
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Recommends:     FlightGear-docs-%{version}
Requires:       liberation-fonts

%description
This package contains the base scenery and aircraft for FlightGear.
It must be installed together with the FlightGear flight simulator package.

%package -n FlightGear-docs
Summary:        FlightGear Documentation
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description -n FlightGear-docs
This package contains pdf, text and html documentation for the
FlightGear flight simulator package.

%prep
%setup -q -n fgdata
dos2unix -c ascii Docs/model-combined.eff/README.model-combined.eff
# Remove no longer used textures
rm -Rf ./Textures/Unused
# Remove texture sources in GIMP format
find . -type f -name \*\.xcf.gz -print -delete
# Delete some build/maintenance scripts
find . -type f -a \( -name \*\.pl -o -name \*\.py -o -name \*\.sh \) -print -delete
# Delete DOS/WINDOWS startup scripts
find . -type f -name \*\.bat -print -delete
# Remove some development files for the Cessna C172p
rm -Rf ./Aircraft/c172p/dev/
# Translation sources (xliff)
find . -type f -name \*FlightGear-nonQt.xlf -print -delete
# More source files
find . -type f -name \*\.zip -print -delete
# Unbundle fonts
rm -Rf ./Fonts/LiberationFonts/

%build
# nothing to do

%install
install -d %{buildroot}%{_datadir}/flightgear

for d in `find ./ -mindepth 1 -maxdepth 1  -type d -not -name Docs` ; do
    cp -R $d %{buildroot}%{_datadir}/flightgear/
done
cp version *.xml %{buildroot}%{_datadir}/flightgear/

# Install docs to default docdir
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
cp -R Docs %{buildroot}%{_defaultdocdir}/%{name}/

# Set permissions for files
find %{buildroot}%{_datadir}/flightgear -type f -exec chmod 0644 "{}" "+"
find %{buildroot}%{_defaultdocdir}/%{name} -type f -exec chmod 0644 "{}" "+"

# Zero length files in docs can be deleted
find %{buildroot}%{_defaultdocdir}/%{name} -type f -empty -print -delete

%fdupes -s %{buildroot}/%{_datadir}/flightgear
%fdupes -s %{buildroot}%{_defaultdocdir}/%{name}

%files
%license COPYING
%{_datadir}/flightgear/

%files -n FlightGear-docs
%doc AUTHORS NEWS README Thanks
%doc %{_defaultdocdir}/%{name}

%changelog
