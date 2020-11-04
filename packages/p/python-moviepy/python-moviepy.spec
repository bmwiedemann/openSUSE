#
# spec file for package python-moviepy
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


%define modname moviepy
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-moviepy
Version:        1.0.2
Release:        0
Summary:        Video editing with Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Zulko/moviepy
Source:         https://files.pythonhosted.org/packages/source/m/moviepy/moviepy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-decorator >= 4.0.2
Requires:       python-numpy
Requires:       python-proglog
Requires:       python-requests >= 2.8.1
Requires:       python-tqdm >= 4.11.2
Recommends:     ImageMagick
Recommends:     ffmpeg
Recommends:     python-Pillow
Recommends:     python-matplotlib >= 2.0.0
Recommends:     python-opencv >= 3.0
Recommends:     python-pygame >= 1.9.3
Recommends:     python-scikit-image >= 0.13.0
Recommends:     python-scikit-learn
Recommends:     python-scipy >= 0.19.0
Recommends:     python-youtube_dl
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module coveralls >= 1.1}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module decorator >= 4.0.2}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module opencv >= 3.0}
BuildRequires:  %{python_module proglog}
BuildRequires:  %{python_module pyOpenSSL >= 0.14}
BuildRequires:  %{python_module pytest >= 3.0.0}
BuildRequires:  %{python_module pytest-cov >= 2.5.1}
BuildRequires:  %{python_module requests >= 2.8.1}
BuildRequires:  %{python_module tqdm >= 4.11.2}
BuildRequires:  ImageMagick
BuildRequires:  ffmpeg
BuildRequires:  python-imageio >= 2.0
BuildRequires:  python-ipaddress
BuildRequires:  python3-imageio >= 2.5
BuildRequires:  python3-imageio-ffmpeg >= 0.2.0
# /SECTION
%ifpython2
Requires:       python-imageio >= 2.1.2
%endif
%ifpython3
Requires:       python-imageio >= 2.5
Requires:       python-imageio-ffmpeg >= 0.2.0
%endif
%python_subpackages

%description
MoviePy is a Python library for video editing. It does
cutting, concatenations, title insertions, video compositing (a.k.a.
non-linear editing), video processing, and creation of custom
effects.

%prep
%setup -q -n moviepy-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests
%{python_expand %fdupes %{buildroot}%{$python_sitelib}
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/moviepy/audio/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/moviepy/audio/
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/moviepy/video/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/moviepy/video/
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/moviepy/video/compositing/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/moviepy/video/compositing/
%fdupes %{buildroot}%{$python_sitelib}
}

# We don’t run test suite, because it depends on ffmpeg and various
# documents downloaded from the Internet.

%files %{python_files}
%doc README.rst
%license LICENCE.txt
%{python_sitelib}/moviepy*

%changelog
