#
# spec file for package python-Kivy
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Kivy
Version:        1.11.1
Release:        0
Summary:        Hardware-accelerated multitouch application library
License:        MIT AND Apache-2.0 AND LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-3.0-only AND BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://kivy.org/
Source:         https://github.com/kivy/kivy/archive/%{version}.tar.gz#/kivy-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module dbus-python}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pyenchant}
BuildRequires:  %{python_module pygments}
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
BuildRequires:  python3-Sphinx
BuildRequires:  xclip
BuildRequires:  xvfb-run
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(pangoft2)
Requires:       mtdev
Requires:       python-Pillow
Requires:       python-Pygments
Requires:       python-docutils
Requires:       python-pyenchant
Requires:       xclip
Recommends:     python-opencv
%python_subpackages

%description
Kivy is a library for development of applications that make use of
user interfaces, such as multi-touch apps.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description    devel
Kivy is a library for development of applications that make use of
user interfaces, such as multi-touch apps.

This package contains the headers and source files for extending kivy

%package     -n %{name}-doc
Summary:        Documentation for Kivy, a multitouch application library
Group:          Documentation/HTML
Provides:       %{python_module Kivy-doc = %{version}}

%description -n %{name}-doc
Kivy is a library for development of applications that make use of
user interfaces, such as multi-touch apps.

%prep
%setup -q -n kivy-%{version}
sed -i "s|data_file_prefix = 'share/kivy-'|data_file_prefix = '%{_docdir}/%{name}-doc/'|" setup.py
# remove shebang
sed -i '1{ /^#!/d; }' kivy/tools/kviewer.py \
  kivy/tools/pep8checker/pep8.py \
  kivy/tools/pep8checker/pre-commit.githook
# remove executable bit
find examples -type f -executable -exec chmod -x {} \;
rm examples/demo/pictures/images/.empty # Remove empty file
rm -r examples/audio # Remove content with non-commercial only license (bnc#749340)
# do not upper restrict cython dep
sed -i -e 's:0\.29\.10:1.0.0:' setup.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build bdist
# create docs
pushd doc
sed -e '/^PYTHON/s/python/python3/' \
    -e '/^SPHINXOPTS	/s/$/ %{?_smp_mflags}/' \
    -i Makefile
export PYTHONPATH=`ls -d ../build/lib*`
make html && rm -r build/html/.buildinfo
popd

%install
%python_install
# workaround to make fdupes its magic as if %%doc macro is used
# would be used after fdupes so rpmlint would complain about duplicates...
install -dm0755 %{buildroot}%{_defaultdocdir}/%{name}-doc
cp -a doc/build/html %{buildroot}/%{_defaultdocdir}/%{name}-doc

%python_expand %fdupes -s %{buildroot}%{$python_sitearch}/kivy
%fdupes -s %{buildroot}%{_defaultdocdir}/%{name}-doc

# Disable tests, they randomly timeout
# %%check
# export DISPLAY=:99.0
# export KIVY_AUDIO=gstplayer # "unable to find ffpyplayer" otherwise
# export LANG=en_US.UTF-8
# %%{python_expand pushd %%{buildroot}%%{$python_sitearch}
# ln -s %%{buildroot}%%{_defaultdocdir}/%%{name}-doc/examples examples
# ln -s %{_builddir}/kivy-%{version}/doc .
# xvfb-run --server-args "-screen 0 1920x1080x24" $python %%{_bindir}/nosetests kivy.tests \
#  -e test_urlrequest -e test_remote_zipsequence
# rm examples doc results.png
# popd
# }

%files %{python_files}
%license LICENSE
%doc AUTHORS
%{python_sitearch}/kivy
%{python_sitearch}/Kivy-%{version}-py*.egg-info
%exclude %{python_sitearch}/kivy/include
%exclude %{python_sitearch}/kivy/tools/gles_compat/gl2.h

%files %{python_files devel}
%{python_sitearch}/kivy/include
%{python_sitearch}/kivy/tools/gles_compat/gl2.h

%files -n %{name}-doc
%doc %{_defaultdocdir}/%{name}-doc

%changelog
