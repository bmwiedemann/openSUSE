#
# spec file for package ddskk
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


# Current version does not build with current xemacs, disable for now
%define use_xemacs 0
Name:           ddskk
Version:        20250328
Release:        0
Summary:        SKK (Simple Kana to Kanji Conversion Program) for Emacs
License:        GPL-2.0-or-later AND SUSE-Permissive AND SUSE-Public-Domain
Group:          Productivity/Editors/Emacs
URL:            http://openlab.ring.gr.jp/skk/ddskk.html
Source0:        https://github.com/skk-dev/ddskk/archive/%{name}-17.1_Neppu.tar.gz
Source1:        suse-start.el
Source97:       update_skkdic.py
Source98:       README.SUSE
Source99:       ddskk-rpmlintrc
Patch2:         bugzilla-141756-workaround.patch
# PATCH-FIX-OPENSUSE or UPSTREAM -- drop build date to make build reproducible
Patch3:         ddskk-drop-build-date.patch
BuildRequires:  compface
BuildRequires:  emacs-x11
BuildRequires:  flim
BuildRequires:  w3m
BuildRequires:  xz
%if %{use_xemacs}
BuildRequires:  xemacs-flim
BuildRequires:  xemacs-packages
BuildRequires:  xemacs-semi
%endif
Requires:       apel
Requires:       emacs
Requires:       skkdic
Provides:       locale(emacs:ja)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
SKK (Simple Kana to Kanji conversion program) is a Japanese input
method for Emacs. ddskk (Daredevil SKK) is a version of SKK that is
aggressively developed.

%if %{use_xemacs}

%package -n ddskk-xemacs
Summary:        SKK (`Simple Kana to Kanji conversion program') for XEmacs
Group:          Productivity/Editors/Emacs
Requires:       skkdic
Requires:       xemacs
Requires:       xemacs-packages
Provides:       locale(xemacs:ja)

%description -n ddskk-xemacs
SKK (`Simple Kana to Kanji conversion program') is a Japanese input
method for XEmacs. ddskk ('Daredevil SKK') is a version of SKK which is
aggressively developed.

%endif

%prep
%autosetup -p1 -n ddskk-ddskk-17.1_Neppu

%build
%define emacs_sitelisp_dir %{_datadir}/emacs/site-lisp
%define emacs_package_dir %{emacs_sitelisp_dir}/skk
(cat >> SKK-CFG)<<-'EOF'
	(setq PREFIX "%{buildroot}%{_prefix}")
	(setq SKK_DATADIR "%{buildroot}%{_datadir}/skk")
	(setq SKK_INFODIR "%{buildroot}%{_infodir}")
	(setq APEL_DIR "%{buildroot}%{emacs_sitelisp_dir}/apel")
	(setq SKK_LISPDIR "%{buildroot}%{emacs_package_dir}")
	EOF
export LANG=ja_JP.UTF-8
make EMACS=emacs %{?_smp_mflags}

%install
export LANG=ja_JP.UTF-8
mkdir -p %{buildroot}%{emacs_package_dir}
make EMACS=emacs install
(cat > %{buildroot}%{emacs_sitelisp_dir}/suse-start-%{name}.el)<<-'EOF'
	;; %{emacs_sitelisp_dir}/suse-start-%{name}.el
	(add-to-list 'load-path "%{emacs_package_dir}")
	EOF
cat %{_sourcedir}/suse-start.el >> %{buildroot}%{emacs_sitelisp_dir}/suse-start-%{name}.el
(cat >> %{buildroot}%{emacs_sitelisp_dir}/suse-start-%{name}.el)<<-'EOF'
	;; %{emacs_sitelisp_dir}/suse-start-%{name}.el ends here
	EOF
######################################################################
%if %{use_xemacs}
# now build for XEmacs:
%define xemacs_package_dir %{_datadir}/xemacs/site-packages/
make clean
sed -ri 's@\(setq[[:blank:]].*\)@@' SKK-CFG
(cat >> SKK-CFG)<<-'EOF'
	(setq PREFIX "%{buildroot}%{_prefix}")
	(setq SKK_DATADIR "%{buildroot}%{_datadir}/skk")
	(setq SKK_INFODIR "%{buildroot}%{xemacs_package_dir}/info")
	(setq APEL_DIR "%{buildroot}%{xemacs_package_dir}/lisp/apel")
	(setq SKK_LISPDIR "%{buildroot}%{xemacs_package_dir}/lisp/skk")
	(setq PACKAGEDIR "%{buildroot}%{xemacs_package_dir}")
	EOF
make EMACS=xemacs %{?_smp_mflags}
make EMACS=xemacs install-package
gzip %{buildroot}%{xemacs_package_dir}/info/skk*.info*

# It would be wasteful if XEmacs had it's own copy of the dictionaries
# and some other files. The whole %{xemacs_package_dir}/etc/skk
# can be shared with Emacs.
rm -rf %{buildroot}%{xemacs_package_dir}%{_sysconfdir}/skk
ln -s %{_datadir}/skk %{buildroot}%{xemacs_package_dir}%{_sysconfdir}/skk
# the info pages are in the skkdic package to be able to share them
# for Emacs and XEmacs:
rm -f %{buildroot}%{xemacs_package_dir}/info/skk*
# replace buildroot in comments in .elc files by spaces with the same total length:
RPM_BUILD_ROOT_REPLACEMENT=$(echo %{buildroot} | tr [:print:] ' ')
for i in $(find %{buildroot} -name "*.elc")
do
    perl -pi -e "s|(;;; from file )%{buildroot}(%{_datadir}/xemacs/site-packages/.*)|\1%{buildroot}\2|" $i
done
%endif
# remove buildroot in .el files
perl -pi -e "s|%{buildroot}||" %{buildroot}%{emacs_package_dir}/skk-setup.el

rm -vf %{buildroot}%{_infodir}/dir
%if %{use_xemacs}
rm -vf %{buildroot}%{xemacs_package_dir}/info/dir
%endif
mv READMEs/INSTALL .

%post
%install_info --info-dir=%{_infodir} %{_infodir}/skk.info

%preun
if test $1 = 0; then
   %install_info_delete --info-dir=%{_infodir} %{_infodir}/skk.info
fi

%files
%defattr(-,root,root)
%doc ChangeLog* READMEs
%{emacs_package_dir}
%config %{emacs_sitelisp_dir}/suse-start-%{name}.el
%dir %{_datadir}/skk/
%{_datadir}/skk/NICOLA-SKK.tut
%{_datadir}/skk/SKK.tut
%{_datadir}/skk/SKK.tut.E
%{_datadir}/skk/skk.xpm
%{_infodir}/*

%if %{use_xemacs}
%files -n ddskk-xemacs
%defattr(-,root,root)
%doc ChangeLog* READMEs
%dir %{xemacs_package_dir}/
%dir %{xemacs_package_dir}/lisp/
%dir %{xemacs_package_dir}%{_sysconfdir}/
%{xemacs_package_dir}/lisp/*
%{xemacs_package_dir}%{_sysconfdir}/*
%endif

%changelog