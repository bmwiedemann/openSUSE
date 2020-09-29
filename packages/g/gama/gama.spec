#
# spec file for package gama
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


Name:           gama
Version:        2.10
Release:        0
Summary:        Adjustment of geodetic networks
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Other
URL:            https://www.gnu.org/software/gama/
# git: http://git.savannah.gnu.org/cgit/gama.git
Source:         http://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Source2:        http://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source3:        http://savannah.gnu.org/project/memberlist-gpgkeys.php?group=%{name}&download=1#/%{name}.keyring
Source4:        %{name}-rpmlintrc
BuildRequires:  gcc-c++
BuildRequires:  libxml2-tools
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(expat) >= 1.1
BuildRequires:  pkgconfig(sqlite3)
# for xmllint
Requires:       libxml2-tools
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
GNU Gama is a project dedicated to adjustment of geodetic networks. It is intended for use with traditional geodetic surveyings which are still used and needed in special measurements (e.g., underground or high precision engineering measurements) where the Global Positioning System (GPS) cannot be used.

Adjustment in local Cartesian coordinate systems is fully supported by a command-line program gama-local that adjusts geodetic (free) networks of observed distances, directions, angles, height differences, 3D vectors and observed coordinates (coordinates with given variance-covariance matrix). Adjustment in global coordinate systems is supported only partly as a gama-g3 program.

%prep
%setup -q
# spurious-executable-perm
chmod -v a-x COPYING ChangeLog* README NEWS TODO AUTHORS

%build
%configure
%make_build

%install
%make_install

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%license COPYING
%doc ChangeLog* README NEWS TODO AUTHORS
%{_bindir}/%{name}-*
%{_infodir}/%{name}.info%{?ext_info}

%changelog
