#
# spec file for package stardict-tools
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           stardict-tools
Version:        3.0.1
Release:        0
Summary:        StarDict Editor
License:        GPL-2.0+
Group:          Productivity/Office/Dictionary
Url:            http://stardict.sourceforge.net
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}.README.SUSE
Source2:        stardict-editor.png
Source3:        stardict-tools-rpmlintrc
Patch1:         stardict-tools-3.0.1-includes.patch
Patch2:         stardict-tools-3.0.1-destbufferoverflow.patch
Patch3:         stardict-tools-3.0.1-gcc44.patch
Patch4:         stardict-tools-3.0.1-gcc6.patch
Patch5:         stardict-tools-3.0.1-wikipediaImage.patch
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel >= 2.6.0
BuildRequires:  pcre-devel
BuildRequires:  update-desktop-files
Recommends:     dictd
%if 0%{?suse_version} < 1010
BuildRequires:  pkgconfig
%else
BuildRequires:  libtool
BuildRequires:  pkgconfig
%endif
%if 0%{?suse_version} > 1020
BuildRequires:  libmysqlclient-devel
%else
BuildRequires:  mysql-devel
%endif

%description
This package contains the dictionary conversion tools which can convert
dictionaries of DICT, wquick, mova and pydict to stardict format.

%prep
%setup -q
%patch1 -p1
%patch2
%patch3
%patch4 -p1
%patch5 -p1

%build
autoreconf -fiv
%configure --with-pic --disable-static
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
install -d -m755 %{buildroot}/%{_libdir}/%{name}
install -d -m755 %{buildroot}/%{_datadir}/{%{name},pixmaps}
install -d -m755 %{buildroot}/%{_defaultdocdir}/%{name}
pushd src 1>/dev/null
# install noinst_PROGRAMS in libdir
for file in $(grep noinst_PROGRAMS Makefile.am | sed -e 's/noinst_PROGRAMS = //'); do
	if test -x $file; then
		if [[ $file == *.exe ]]; then
			continue;
		else
			install -m755 $file %{buildroot}/%{_libdir}/%{name}/
		fi;
	fi
done
# install scripts in sharedir
for file in uyghur2dict.py mkguangyunst.py stmerge.py KangXiZiDian-djvu2tiff.py; do
	echo '#!%{_bindir}/python' > "${file}.tmp"
	cat "$file" >> "${file}.tmp"
	mv -f "${file}.tmp" "$file"
	chmod 755 "$file"
done
for file in *.py *.pl *.perl; do
  dos2unix -q -n $file %{buildroot}/%{_datadir}/%{name}/$file
  sed -i 's|^#!%{_bindir}/env python.*|#!%{_bindir}/python|' %buildroot/%{_datadir}/%{name}/$file
  chmod 755 %{buildroot}/%{_datadir}/%{name}/$file
done
popd 1>/dev/null
# install documentation
sed -e "s#__LIBDIR__#%{_libdir}#g" %{SOURCE1} > %buildroot/%{_defaultdocdir}/%{name}/README.SUSE
install -m644 AUTHORS ChangeLog COPYING README %{buildroot}/%{_defaultdocdir}/%{name}/
# install desktop entry
install -m644 %{SOURCE2} %{buildroot}/%{_datadir}/pixmaps/
%suse_update_desktop_file -c stardict-editor "Stardict Dictionary Editor" "Editor for stardict dictionaries" stardict-editor stardict-editor.png Office Dictionary

%files
%defattr(-, root, root)
%doc %{_defaultdocdir}/%{name}
%{_bindir}/stardict-editor
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/stardict-editor.png
%{_datadir}/applications/stardict-editor.desktop

%changelog
