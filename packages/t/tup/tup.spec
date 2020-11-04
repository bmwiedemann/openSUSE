#
# spec file for package tup
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


Name:           tup
Version:        0.7.10
Release:        0
Summary:        File-based build system
License:        GPL-2.0-only
URL:            http://gittup.org/tup/
Source0:        https://github.com/gittup/tup/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       %{name}.rpmlintrc
Patch0:         tup-add_archs.patch
# PATCH-FIX-UPSTREAM tup-32bit.patch
Patch1:         tup-32bit.patch
BuildRequires:  awk
BuildRequires:  pkgconfig
BuildRequires:  vim
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libpcre)
Requires:       vim

%description
Tup is a file-based build system.
It inputs a list of file changes and a directed acyclic graph (DAG),
then processes the DAG to execute the appropriate commands required
to update dependent files.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    doc
Documents and examples for %{name}

%prep
%autosetup -p1
sed "s/\`git describe\`/%{version}/" -i src/tup/link.sh

%build
export CFLAGS="%{optflags}"
./build.sh
./build/tup init
./build/tup generate runme.sh
./runme.sh

%install
vimver=$(vim --version|grep ^VIM|awk '{gsub("\\.","",$5); print $5}')
gzip tup.1
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1 \
         %{buildroot}%{_datadir}/vim/vim$vimver/syntax \
         %{buildroot}%{_datadir}/vim/vim$vimver/ftdetect
install -m755 tup -t %{buildroot}%{_bindir}
install -m644 tup.1.gz -t %{buildroot}%{_mandir}/man1
install -m644 contrib/syntax/tup.vim -t %{buildroot}%{_datadir}/vim/vim$vimver/syntax
echo 'au BufNewFile,BufRead Tupfile,*.tup setf tup' > %{buildroot}%{_datadir}/vim/vim$vimver/ftdetect/tup.vim
echo -e "%{_datadir}/vim/vim$vimver/syntax/tup.vim\n%{_datadir}/vim/vim$vimver/ftdetect\n" > vim.files
rm docs/html/*.sh docs/html/Tupfile
mv docs/html/pub/*.pdf docs/html/
mv docs/html/pub/*.css docs/html/
rm -rf docs/html/pub

%files -f vim.files
%doc CONTRIBUTING.md README.md
%license COPYING
%{_bindir}/tup
%{_mandir}/man1/tup.1.gz

%files doc
%doc docs/*

%changelog
