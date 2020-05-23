#
# spec file for package python-pymavlink
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


%define binaries mavtomfile mavtogpx mavsummarize mavsigloss mavsearch mavplayback mavparms mavparmdiff mavmission mavloss mavlogdump mavlink_bitmask_decoder mavkml mavgraph mavgpslock mavgen mavflighttime mavflightmodes mavfft_isb mavfft mavextract magfit_motors magfit_gps magfit_delta magfit MPU6KSearch
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pymavlink
Version:        2.4.6
Release:        0
Summary:        Python MAVLink code
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/ArduPilot/pymavlink/
Source:         https://files.pythonhosted.org/packages/source/p/pymavlink/pymavlink-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-future
Requires:       python-lxml
Requires(post): update-alternatives
Requires(postun): update-alternatives
# SECTION test requirements
BuildRequires:  %{python_module lxml}
# /SECTION
%python_subpackages

%description
A Python library for handling MAVLink protocol streams and log files.
This allows for the creation of simple scripts to analyse telemetry
logs from autopilots such as ArduPilot which use the MAVLink protocol.

%prep
%setup -q -n pymavlink-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
# drop shebang
%python_expand find %{buildroot}%{$python_sitearch} -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;
# FIXME: remove devel files for now
%python_expand rm -rf %{buildroot}%{$python_sitearch}/pymavlink/generator/C
%python_expand rm -rf %{buildroot}%{$python_sitearch}/pymavlink/generator/CPP11
%python_expand rm -rf %{buildroot}%{$python_sitearch}/pymavlink/mavnative/mavlink_defaults.h
# fix spurious exec permissions
%python_expand find %{buildroot}%{$python_sitearch} -name "*.xml" -exec chmod -x '{}' \;
# strip .py file extension from scripts
%python_expand cd %{buildroot}%{_bindir} && find . -name "*.py" -exec sh -c 'mv $0 `basename "$0" .py`' '{}' \;
for b in %{binaries}; do
  %python_clone -a %{buildroot}%{_bindir}/$b
done
#
%python_expand %fdupes %{buildroot}%{$python_sitearch}
# remove unneeded files
rm -f %{buildroot}%{_bindir}/_current_flavor

%check
# FIXME: testsuite does not run in OBS
#%%python_exec setup.py test

%post
for b in %{binaries}; do
  %python_install_alternative $b
done

%postun
for b in %{binaries}; do
  %python_uninstall_alternative $b
done

%files %{python_files}
%doc README.md
%python_alternative %{_bindir}/MPU6KSearch
%python_alternative %{_bindir}/magfit
%python_alternative %{_bindir}/magfit_delta
%python_alternative %{_bindir}/magfit_gps
%python_alternative %{_bindir}/magfit_motors
%python_alternative %{_bindir}/mavextract
%python_alternative %{_bindir}/mavfft
%python_alternative %{_bindir}/mavfft_isb
%python_alternative %{_bindir}/mavflightmodes
%python_alternative %{_bindir}/mavflighttime
%python_alternative %{_bindir}/mavgen
%python_alternative %{_bindir}/mavgpslock
%python_alternative %{_bindir}/mavgraph
%python_alternative %{_bindir}/mavkml
%python_alternative %{_bindir}/mavlink_bitmask_decoder
%python_alternative %{_bindir}/mavlogdump
%python_alternative %{_bindir}/mavloss
%python_alternative %{_bindir}/mavmission
%python_alternative %{_bindir}/mavparmdiff
%python_alternative %{_bindir}/mavparms
%python_alternative %{_bindir}/mavplayback
%python_alternative %{_bindir}/mavsearch
%python_alternative %{_bindir}/mavsigloss
%python_alternative %{_bindir}/mavsummarize
%python_alternative %{_bindir}/mavtogpx
%python_alternative %{_bindir}/mavtomfile
%{python_sitearch}/mavnative*.so
%{python_sitearch}/pymavlink*

%changelog
