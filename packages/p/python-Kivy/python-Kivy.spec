#
# spec file for package python-Kivy
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


%if %{suse_version} > 1500
%define mypython python3
%define __mypython %{__python3}
%else
%{?sle15_python_module_pythons}
%define mypython %pythons
%define __mypython %{expand:%%__%{pythons}}
%endif
%define plainpython python
Name:           python-Kivy
Version:        2.3.1
Release:        0
Summary:        Hardware-accelerated multitouch application library
License:        Apache-2.0 AND MIT AND LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-3.0-only AND BSD-3-Clause
URL:            https://kivy.org/
Source:         https://github.com/kivy/kivy/archive/%{version}.tar.gz#/kivy-%{version}.tar.gz
Source99:       python-Kivy.rpmlintrc
BuildRequires:  %{mypython}-Sphinx
BuildRequires:  %{python_module Cython with %python-Cython < 3}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module dbus-python}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyenchant}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  Mesa-devel
BuildRequires:  Mesa-dri
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  dbus-1
BuildRequires:  fdupes
BuildRequires:  gstreamer-plugins-bad
BuildRequires:  gstreamer-plugins-good
BuildRequires:  mtdev
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  xclip
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(pangoft2)
Requires:       mtdev
Requires:       python-Pygments
Requires:       python-docutils
Requires:       python-filetype
Requires:       xclip
# Not listed in setup.cfg but imported in core/spelling/spelling_enchant.py
Requires:       python-pyenchant
# SECTION extra [base] (and [full])
Requires:       python-Pillow
Requires:       python-requests
# /SECTION
# SECTION test
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module filetype}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module responses}
# /SECTION
# Section doc
BuildRequires:  %{mypython}-Sphinx
BuildRequires:  %{mypython}-sphinxcontrib-jquery
#BuildRequires:  %%{mypython}-sphinxcontrib-actdiag
#BuildRequires:  %%{mypython}-sphinxcontrib-blockdiag
#BuildRequires:  %%{mypython}-sphinxcontrib-nwdiag
#BuildRequires:  %%{mypython}-sphinxcontrib-seqdiag
# /SECTION
Recommends:     python-opencv
%python_subpackages

%description
Kivy is a library for development of applications that make use of
user interfaces, such as multi-touch apps.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       %plainpython(abi) = %{python_version}

%description    devel
Kivy is a library for development of applications that make use of
user interfaces, such as multi-touch apps.

This package contains the headers and source files for extending kivy

%package     -n %{name}-doc
Summary:        Documentation for Kivy, a multitouch application library
Provides:       %{python_module Kivy-doc = %{version}}
BuildArch:      noarch

%description -n %{name}-doc
Kivy is a library for development of applications that make use of
user interfaces, such as multi-touch apps.

%prep
%setup -q -n kivy-%{version}
# remove the legacy garden install script as python requirement, get it from PyPI or https://github.com/kivy-garden/garden/ if you need it
sed -i '/Kivy-Garden/d' setup.cfg
# remove shebang
sed -i '1{ /^#!/d; }' kivy/tools/kviewer.py \
  kivy/tools/pep8checker/pep8.py \
  kivy/tools/pep8checker/pre-commit.githook
# remove executable bit
find examples -type f -executable -exec chmod -x {} \;
rm examples/demo/pictures/images/.empty # Remove empty file
rm -r examples/audio # Remove content with non-commercial only license (bnc#749340)
# fix shebang
sed -i "/^#!/ c #!%{__mypython}" kivy/tools/image-testsuite/gimp28-testsuite.py
sed -i "/^#!/ c #!`which sh`" kivy/tools/image-testsuite/imagemagick-testsuite.sh
# remove benchmark from tests
sed -i /addopts/d pyproject.toml
chmod -x kivy/tools/pep8checker/pre-commit.githook

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export KIVY_SPLIT_EXAMPLES=1
%pyproject_wheel
# create docs
pushd doc
sed -e '/^PYTHON/ s|python|%{__mypython}|' \
    -e '/^SPHINXOPTS	/s/$/ %{?_smp_mflags}/' \
    -i Makefile
export PYTHONPATH=`ls -d ../build/lib*`
make %{?_smp_mflags} PYTHON=%{__mypython} html && rm -r build/html/.buildinfo
popd

%install
%pyproject_install
%{python_expand #
%fdupes %{buildroot}%{$python_sitearch}/kivy
find %{buildroot}%{$python_sitearch}/kivy -name '*.h' \
  | sed 's|%{buildroot}||' \
  | tee kivy-devel-%{$python_bin_suffix}.files \
  | sed 's|^/|%%exclude /|' > kivy-exclude-devel-%{$python_bin_suffix}.files
}
# workaround to make fdupes its magic as if %%doc macro is used
# would be used after fdupes so rpmlint would complain about duplicates...
install -dm0755 %{buildroot}%{_docdir}/%{name}-doc
cp -a doc/build/html %{buildroot}/%{_docdir}/%{name}-doc/
cp -a examples %{buildroot}/%{_docdir}/%{name}-doc/
%fdupes %{buildroot}%{_docdir}/%{name}-doc

%check
# we don't care about speed inside obs
donttest="benchmark"
# no network (or localhost resolution) in obs
donttest="$donttest or test_urlrequest_urllib or test_remote_zipsequence"
# avoid collection errors
mv kivy kivy.notinpath
pushd examples
%pytest_arch --pyargs kivy -k "not ($donttest)"
popd

%files %{python_files} -f kivy-exclude-devel-%{python_bin_suffix}.files
%license LICENSE
%doc AUTHORS
%{python_sitearch}/kivy
%{python_sitearch}/Kivy-%{version}.dist-info

%files %{python_files devel} -f kivy-devel-%{python_bin_suffix}.files
%doc doc/sources/changelog.rst

%files -n %{name}-doc
%doc %{_docdir}/%{name}-doc

%changelog
