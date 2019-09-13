#
# spec file for package bpython
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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
#


Name:           bpython
Version:        0.15
Release:        0
Url:            http://www.bpython-interpreter.org
Summary:        Fancy Curses Interface to the Python Interactive Interpreter
License:        MIT
Group:          Development/Languages/Python
Source:         http://www.bpython-interpreter.org/releases/bpython-%{version}.tar.gz
Source1:        bpython-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-six
BuildRequires:  update-desktop-files
# Documentation requirements:
BuildRequires:  python-Sphinx
# Test requirements:
BuildRequires:  python-curses
BuildRequires:  python-mock
BuildRequires:  python-nose
Requires:       python-Pygments
Requires:       python-curses
Requires:       python-curtsies
Requires:       python-greenlet
Requires:       python-jedi
Requires:       python-pyparsing
Requires:       python-six
Requires(post): update-alternatives
Requires(preun): update-alternatives
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
Bpython is an enhanced Python interactive interpreter that uses curses
and provides the following main features: in-line syntax highlighting;
readline-like autocompletion with suggestions displayed as you type; expected
argument specification for functions; a handy pastebin function to quickly
submit your code and return a URL. Its goal is to bring together a few handy
ideas to enhance the standard interpreter without getting carried away.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
Recommends:     %{name} = %{version}

%description doc
Documentation and help files for %{name}.

%prep
%setup -q -n bpython-%{version}

mv data/bpython.desktop data/bpython2.desktop
mv data/bpython.png data/bpython2.png
mv data/bpython.appdata.xml data/bpython2.appdata.xml

sed -i -e "s|Icon=bpython|Icon=bpython2|" \
       -e "s|Exec=/usr/bin/bpython|Exec=bpython-%{py_ver}|" data/bpython2.desktop
sed -i "s|bpython.desktop|bpython2.desktop|" data/bpython2.appdata.xml
sed -i -e "s|bpython.desktop|bpython2.desktop|" \
       -e "s|bpython.png|bpython2.png|" \
       -e "s|bpython.appdata.xml|bpython2.appdata.xml|" setup.py

%build
export LC_ALL=en_US.utf8
python setup.py build
python setup.py build_sphinx && rm build/sphinx/html/.buildinfo # HTML documentation

gzip build/man/bpython.1
gzip build/man/bpython-config.5

%install
export LC_ALL=en_US.utf8
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for p in bpdb bpython bpython-urwid bpython-curses ; do
    mv %{buildroot}%{_bindir}/$p %{buildroot}%{_bindir}/$p-%{py_ver}
    ln -s -f %{_sysconfdir}/alternatives/$p %{buildroot}%{_bindir}/$p
done

install -d %{buildroot}%{_mandir}/man1/
install -m 644 build/man/bpython.1 %{buildroot}%{_mandir}/man1/bpython-%{py_ver}.1
gzip %{buildroot}%{_mandir}/man1/bpython.1
mv %{buildroot}%{_mandir}/man1/bpython.1.gz %{buildroot}%{_mandir}/man1/bpython-%{py_ver}.1.gz
ln -s -f %{_sysconfdir}/alternatives/bpython.1.gz %{buildroot}%{_mandir}/man1/bpython.1.gz

install -d %{buildroot}%{_mandir}/man5/
install -m 644 build/man/bpython-config.5 %{buildroot}%{_mandir}/man5/bpython-config-%{py_ver}.5
gzip %{buildroot}%{_mandir}/man5/bpython-config.5
mv %{buildroot}%{_mandir}/man5/bpython-config.5.gz %{buildroot}%{_mandir}/man5/bpython-config-%{py_ver}.5.gz
ln -s -f %{_sysconfdir}/alternatives/bpython-config.5.gz %{buildroot}%{_mandir}/man5/bpython-config.5.gz

rm -r %{buildroot}%{python_sitelib}/bpython/test # Don't ship tests
%if 0%{?suse_version}
%suse_update_desktop_file -G bpython -r bpython2 Development IDE
%endif

#NOTE(saschpe): Check the one failing test
#%%check
#nosetests

%post
%_sbindir/update-alternatives \
    --install %{_bindir}/bpython bpython %{_bindir}/bpython-%{py_ver} 30 \
    --slave %{_bindir}/bpdb bpdb %{_bindir}/bpdb-%{py_ver} \
    --slave %{_bindir}/bpython-curses bpython-curses %{_bindir}/bpython-curses-%{py_ver} \
    --slave %{_bindir}/bpython-urwid bpython-urwid %{_bindir}/bpython-urwid-%{py_ver} \
    --slave %{_mandir}/man1/bpython.1.gz bpython.1.gz %{_mandir}/man1/bpython-%{py_ver}.1.gz \
    --slave %{_mandir}/man5/bpython-config.5.gz bpython-config.5.gz %{_mandir}/man5/bpython-config-%{py_ver}.5.gz

%preun
if [ $1 -eq 0 ] ; then
    %_sbindir/update-alternatives --remove bpython %{_bindir}/bpython-%{py_ver}
fi

%files
%defattr(-,root,root)
%doc AUTHORS CHANGELOG LICENSE README.rst
%{_bindir}/bpdb
%{_bindir}/bpython
%{_bindir}/bpython-curses
%{_bindir}/bpython-urwid
%{_bindir}/bpdb-%{py_ver}
%{_bindir}/bpython-%{py_ver}
%{_bindir}/bpython-curses-%{py_ver}
%{_bindir}/bpython-urwid-%{py_ver}
%ghost %{_sysconfdir}/alternatives/bpdb
%ghost %{_sysconfdir}/alternatives/bpython
%ghost %{_sysconfdir}/alternatives/bpython-curses
%ghost %{_sysconfdir}/alternatives/bpython-urwid
%{_mandir}/man1/bpython.1.gz
%{_mandir}/man5/bpython-config.5.gz
%{_mandir}/man1/bpython-%{py_ver}.1.gz
%{_mandir}/man5/bpython-config-%{py_ver}.5.gz
%ghost %{_sysconfdir}/alternatives/bpython.1.gz
%ghost %{_sysconfdir}/alternatives/bpython-config.5.gz
%{python_sitelib}/bpdb
%{python_sitelib}/bpython-%{version}-py*.egg-info
%{python_sitelib}/bpython/
%if %{suse_version} <= 1315
%dir %{_datadir}/appdata
%endif
%{_datadir}/appdata/bpython2.appdata.xml
%{_datadir}/applications/bpython2.desktop
%{_datadir}/pixmaps/bpython2.png

%files doc
%defattr(-,root,root)
%doc build/sphinx/html

%changelog
