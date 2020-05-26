#
# spec file for package python-pastream
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-pastream
Version:        0.2.0.post0
Release:        0
Summary:        GIL-less Portaudio Streams for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/tgarc/pastream
Source0:        https://files.pythonhosted.org/packages/source/p/pastream/pastream-%{version}.tar.gz
Source100:      python-pastream-rpmlintrc
BuildRequires:  %{python_module cffi >= 1.4.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pa-ringbuffer >= 0.1.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(portaudiocpp)
Requires:       libsndfile
Requires:       portaudio
Requires:       python-SoundFile >= 0.9.0
Requires:       python-cffi >= 1.0.0
Requires:       python-pa-ringbuffer >= 0.1.2
Requires:       python-sounddevice >= 0.3.9
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-numpy
# SECTION test requirements
BuildRequires:  %{python_module SoundFile >= 0.9.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest >= 3.0}
BuildRequires:  %{python_module sounddevice >= 0.3.9}
# /SECTION
%python_subpackages

%description
Pastream builds on top of portaudio and sounddevice python bindings
to provide some more functionality. Note that in addition to the
pastream library, pastream includes a command line application for
playing and recording audio files.

%prep
%setup -q -n pastream-%{version}
sed -i -e '/^#!\//, 1d' src/pastream.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pastream
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# Tests require an audio device
# %%check
# pushd tests
# %%{python_expand export PYTHONPATH=%%{buildroot}%%{$python_sitearch}
# py.test-%%{$python_bin_suffix} .
# }
# popd

%post
%python_install_alternative pastream

%postun
%python_uninstall_alternative pastream

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/pastream
%{python_sitearch}/*

%changelog
