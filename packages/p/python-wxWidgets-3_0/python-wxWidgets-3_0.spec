#
# spec file for package python-wxWidgets-3_0
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


%define srcname wxPython
%define wx_version %(echo "%version" | perl -pe 's{\\.\\d+\\.\\d+$}{}')
%define wx_release %(echo "%version" | perl -pe 's{\\.\\d+$}{}')
Name:           python-wxWidgets-3_0
Version:        3.0.2.0
Release:        0
Summary:        Python Bindings for wxWidgets
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            http://www.wxpython.org/
# Source from http://www.wxpython.org/ contains complete wxWidgets
# source tree and proprietary Microsoft Visual Studio DLLs.
# We will repackage only a needed subset of files.
#DL-URL:	http://downloads.sourceforge.net/wxpython/%srcname-src-%version.tar.bz2
Source:         %srcname-%version.tar.xz
Source2:        %name-rpmlintrc
Source3:        extract-source.sh
Source4:        pre_checkin.sh
Patch1:         wxPython-platlib.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  python-rpm-macros
BuildRequires:  python2-devel
BuildRequires:  python2-xml
BuildRequires:  wxWidgets-3_0-devel
BuildRequires:  xz
Requires(post): update-alternatives
Requires(postun): update-alternatives
# In fact it should be >= %version but only version < 3.1
Recommends:     %name-lang = %version
Conflicts:      python-wxWidgets
Conflicts:      python2-wxWidgets
#Requires:       wxWidgets-3_0 = %(rpm -q --qf="%%VERSION" wxWidgets-3_0)
# Used up to openSUSE 11.3:
Provides:       python-wxGTK = %version
Obsoletes:      python-wxGTK < %version
# Upstream name, never used in SUSE:
Provides:       wxPython = %version
# Third party packages name, never used in SUSE:
Provides:       python-wxWidgets = %version
Provides:       python2-wxWidgets = %version
Provides:       wxPython%wx_version-gtk2-unicode = %version

%description
wxWidgets is a C++ library for cross-platform GUI.
This package contains the Python bindings for wxWidgets.

%package devel
Summary:        Everything needed for development with wxPython
Group:          Development/Languages/Python
Requires:       %name = %version
Conflicts:      python-wxWidgets-devel
Provides:       python-wxWidgets-devel = %version

%description devel
wxWidgets is a C++ library for cross-platform GUI development. With
wxWidgets, applications for different GUIs (GTK+, Motif, MS Windows,
MacOS X, Windows CE, GPE) can be created from the same source code.

This package contains all files needed for developing with Python
bindings for wxGTK.

%package lang
# We cannot use %%lang_package here. Editra translations use noarch incompatible path.
Summary:        Languages for package python-wxWidgets
Group:          System/Localization
Requires:       %name = %version
Supplements:    packageand(bundle-lang-other:%name)
Provides:       %name-lang-all = %version

%description lang
Provides translations to the package %name.

%prep
%setup -q -n %srcname-src-%version
%patch -P 1 -p1

%build
pushd wxPython/

# kill off outdated header copies, use system headers instead
mv include/wx/wxPython wxpyinc
rm -Rf include/wx/
mkdir -p include/wx
mv wxpyinc include/wx/wxPython

python2 setup.py build
popd

%install
# bnc#740950… python-wxWidgets version a.b.c.d wants to run with wxWidgets
# a.b.c only. This however is not always possible: at the time of this writing,
# wxWidgets was already at 3.0.1 but most recent wxPython version is 3.0.0.
# The version mismatch causes a warning, but it might be fine if we ensure that
# the python module runs against the precise version *it was built with*.
pushd wxPython/
python2 setup.py install --prefix="%_prefix" --root="%buildroot"
popd

# Create %%lang tags for mo files in non-standard path:
echo "%%defattr(-,root,root)" >Editra.lang
for LNG_DIR in "%buildroot%python_sitearch"/wx*/wx/tools/Editra/locale/*; do
	LNG="${LNG_DIR##*/}"
	echo "%%lang($LNG) %%python_sitearch${LNG_DIR#%buildroot%python_sitearch}" >>Editra.lang
done

mkdir -p %buildroot/%_sysconfdir/alternatives
for f in pywxrc editra helpviewer img2png img2py img2xpm pyalacarte pyalamode pycrust pyshell pywrap xrced ; do
mv "%buildroot/%_bindir/$f" "%buildroot/%_bindir/$f-%python2_bin_suffix"
ln -sf "%_sysconfdir/alternatives/$f" "%buildroot/%_bindir/$f"
done
%fdupes %buildroot/%_prefix

%post
update-alternatives --install %_bindir/pywxrc pywxrc %_bindir/pywxrc-%python2_bin_suffix %python2_version_nodots \
    --slave %_bindir/editra editra %_bindir/editra-%python2_bin_suffix \
    --slave %_bindir/helpviewer helpviewer %_bindir/helpviewer-%python2_bin_suffix \
    --slave %_bindir/img2png img2png %_bindir/img2png-%python2_bin_suffix \
    --slave %_bindir/img2py img2py %_bindir/img2py-%python2_bin_suffix \
    --slave %_bindir/img2xpm img2xpm %_bindir/img2xpm-%python2_bin_suffix \
    --slave %_bindir/pyalacarte pyalacarte %_bindir/pyalacarte-%python2_bin_suffix \
    --slave %_bindir/pyalamode pyalamode %_bindir/pyalamode-%python2_bin_suffix \
    --slave %_bindir/pycrust pycrust %_bindir/pycrust-%python2_bin_suffix \
    --slave %_bindir/pyshell pyshell %_bindir/pyshell-%python2_bin_suffix \
    --slave %_bindir/pywrap pywrap %_bindir/pywrap-%python2_bin_suffix \
    --slave %_bindir/xrced xrced %_bindir/xrced-%python2_bin_suffix \

%postun
if [ ! -f %_bindir/pywxrc ] ; then
   update-alternatives --remove pywxrc %_bindir/pywxrc-%python2_bin_suffix
fi

%files
%defattr(-,root,root)
%license wxPython/licence
%doc wxPython/docs/*.txt wxPython/docs/*.html wxPython/docs/screenshots
%_bindir/editra
%_bindir/helpviewer
%_bindir/img2png
%_bindir/img2py
%_bindir/img2xpm
%_bindir/pyalacarte
%_bindir/pyalamode
%_bindir/pycrust
%_bindir/pyshell
%_bindir/pywrap
%_bindir/pywxrc
%_bindir/xrced
%_bindir/editra-%python2_bin_suffix
%_bindir/helpviewer-%python2_bin_suffix
%_bindir/img2png-%python2_bin_suffix
%_bindir/img2py-%python2_bin_suffix
%_bindir/img2xpm-%python2_bin_suffix
%_bindir/pyalacarte-%python2_bin_suffix
%_bindir/pyalamode-%python2_bin_suffix
%_bindir/pycrust-%python2_bin_suffix
%_bindir/pyshell-%python2_bin_suffix
%_bindir/pywrap-%python2_bin_suffix
%_bindir/pywxrc-%python2_bin_suffix
%_bindir/xrced-%python2_bin_suffix
%ghost %_sysconfdir/alternatives/editra
%ghost %_sysconfdir/alternatives/helpviewer
%ghost %_sysconfdir/alternatives/img2png
%ghost %_sysconfdir/alternatives/img2py
%ghost %_sysconfdir/alternatives/img2xpm
%ghost %_sysconfdir/alternatives/pyalacarte
%ghost %_sysconfdir/alternatives/pyalamode
%ghost %_sysconfdir/alternatives/pycrust
%ghost %_sysconfdir/alternatives/pyshell
%ghost %_sysconfdir/alternatives/pywrap
%ghost %_sysconfdir/alternatives/pywxrc
%ghost %_sysconfdir/alternatives/xrced
%python_sitearch/*
%python_sitelib/*
%exclude %python_sitearch/wx*/wx/tools/Editra/locale/*

%files lang -f Editra.lang

%files devel
%defattr(-,root,root)
%_includedir/wx-%wx_version/

%changelog
