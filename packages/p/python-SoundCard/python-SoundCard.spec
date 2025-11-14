#
# spec file for package python-SoundCard
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-SoundCard
Version:        0.4.5
Release:        0
Summary:        Python package to play and record audio
License:        BSD-3-Clause
URL:            https://github.com/bastibe/SoundCard
Source0:        https://files.pythonhosted.org/packages/source/s/soundcard/soundcard-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/bastibe/SoundCard/master/LICENSE
Source100:      python-SoundCard-rpmlintrc
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module numpy >= 1.11}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?sle_version} && 0%{?sle_version} < 150300
Requires:       pulseaudio
%else
Requires:       pulseaudio-daemon
%endif
Requires:       python-cffi
Requires:       python-numpy
BuildArch:      noarch
%python_subpackages

%description
SoundCard is a library for playing and recording audio without
resorting to a CPython extension. Instead, it is implemented using
CFFI and the native audio libraries of Linux, Windows and macOS.

SoundCard is cross-platform, and supports Linux/pulseaudio,
Mac/coreaudio, and Windows/WASAPI. While the interface is identical
across platforms, naming schemes and block sizes can vary between
devices and platforms.

%prep
%setup -q -n soundcard-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/soundcard
%{python_sitelib}/[Ss]ound[Cc]ard-%{version}.dist-info

%changelog
