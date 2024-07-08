#
# spec file for package python-python-rtmidi
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-python-rtmidi
Version:        1.5.8
Release:        0
Summary:        Python binding for the RtMidi C++ library
License:        MIT
URL:            https://spotlightkid.github.io/python-rtmidi/
Source:         https://files.pythonhosted.org/packages/source/p/python-rtmidi/python_rtmidi-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module meson-python}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  python(abi) > 3.8
%python_subpackages

%description
RtMidi is a set of C++ classes which provides an API for realtime
MIDI I/O across Linux (ALSA & JACK), macOS (CoreMIDI & JACK),
and Windows (MultiMedia System) operating systems.

python-rtmidi is a Python binding for RtMidi implemented using
Cython and provides a thin wrapper around the RtMidi C++ interface.
The API is basically the same as the C++ one but with the naming
scheme of classes, methods and parameters adapted to the Python
PEP-8 conventions and requirements of the Python package naming
structure.

%prep
%setup -q -n python_rtmidi-%{version}
sed -i 's,/usr/bin/env python,%{_bindir}/%{python_for_executables},' examples/*.py examples/*/*.py
rm src/_rtmidi.cpp

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# not running tests since they require working JACK/ALSA,
# which cannot be provided on OBS workers

%files %{python_files}
%license LICENSE.md
%doc AUTHORS.md CHANGELOG.md README.md
%doc examples
%{python_sitearch}/rtmidi
%{python_sitearch}/python_rtmidi-%{version}.dist-info

%changelog
