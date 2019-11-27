#
# spec file for package python-pymavlink
#
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pymavlink
Version:        2.4.0
Release:        0
License:        LGPL-3.0
Summary:        Python MAVLink code
Url:            https://github.com/ArduPilot/pymavlink/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pymavlink/pymavlink-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module future}
# SECTION test requirements
BuildRequires:  %{python_module lxml}
# /SECTION
BuildRequires:  fdupes
Requires:       python-future
Requires:       python-lxml
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
#
%python_expand %fdupes %{buildroot}%{$python_sitearch}
# remove unneeded files
rm -f %{buildroot}%{_bindir}/_current_flavor

%check
# FIXME: testsuite does not run in OBS
#%%python_exec setup.py test

%files %{python_files}
%doc README.md
%python3_only %{_bindir}/MPU6KSearch
%python3_only %{_bindir}/magfit
%python3_only %{_bindir}/magfit_delta
%python3_only %{_bindir}/magfit_gps
%python3_only %{_bindir}/magfit_motors
%python3_only %{_bindir}/mavextract
%python3_only %{_bindir}/mavfft
%python3_only %{_bindir}/mavfft_isb
%python3_only %{_bindir}/mavflightmodes
%python3_only %{_bindir}/mavflighttime
%python3_only %{_bindir}/mavgen
%python3_only %{_bindir}/mavgpslock
%python3_only %{_bindir}/mavgraph
%python3_only %{_bindir}/mavkml
%python3_only %{_bindir}/mavlink_bitmask_decoder
%python3_only %{_bindir}/mavlogdump
%python3_only %{_bindir}/mavloss
%python3_only %{_bindir}/mavmission
%python3_only %{_bindir}/mavparmdiff
%python3_only %{_bindir}/mavparms
%python3_only %{_bindir}/mavplayback
%python3_only %{_bindir}/mavsearch
%python3_only %{_bindir}/mavsigloss
%python3_only %{_bindir}/mavsummarize
%python3_only %{_bindir}/mavtogpx
%python3_only %{_bindir}/mavtomfile
%{python_sitearch}/mavnative*.so
%{python_sitearch}/pymavlink*

%changelog
