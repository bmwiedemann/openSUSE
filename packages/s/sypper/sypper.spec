# Copyright (C) 2024 SUSE LLC
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, see <http://www.gnu.org/licenses/>.

Name:           sypper
Version:        0.06
Release:        0
License:        GPL-2.0-or-later
Summary:        Simple perl utility emulating zypper download
Group:          System/Packages
Url:            https://github.com/andrii-suse/sypper
Source:         %{name}-%{version}.tar.xz
%{perl_requires}
Requires:       perl-base = %{perl_version}
Requires:       perl-solv
Requires:       perl-Mojolicious
Requires:       perl-Config-IniFiles
BuildRequires:  make
BuildArch:      noarch

%description
Investigate and benchmark various package download strategies

%prep
%setup -q

%build

%install
%make_install
mkdir -p %{buildroot}%{_bindir}
ln -s %{_datadir}/sypper/script/sypper %{buildroot}%{_bindir}/sypper

%files
%{_datadir}/sypper
%{_bindir}/sypper


%changelog

