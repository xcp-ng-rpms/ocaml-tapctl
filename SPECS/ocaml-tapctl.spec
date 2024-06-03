%global package_speccommit d1317a1b321c54125f3bf4356c85ed8b27efaecf
%global package_srccommit v1.5.1
%global debug_package %{nil}

Name:           ocaml-tapctl
Version: 1.5.1
Release: 15.1%{?xsrel}%{?dist}
Summary:        Manipulate running tapdisk instances
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/xapi-project/tapctl
Source0: tapctl-1.5.1.tar.gz
BuildRequires:  xs-opam-repo
BuildRequires:  forkexecd-devel

%description
Manipulate running tapdisk instances on a xen host.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       forkexecd-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%global ocaml_dir %{_opamroot}/ocaml-system
%global ocaml_libdir %{ocaml_dir}/lib
%global ocaml_docdir %{ocaml_dir}/doc

%prep
%autosetup -p1

%build
make

%check
make test

%install
mkdir -p %{buildroot}%{ocaml_libdir}
mkdir -p %{buildroot}%{ocaml_docdir}
make install OPAM_PREFIX=%{buildroot}%{ocaml_dir} OPAM_LIBDIR=%{buildroot}%{ocaml_libdir}

%files
%doc ChangeLog
%doc LICENSE
%doc MAINTAINERS
%doc README.md
%{ocaml_libdir}/xapi-tapctl
%exclude %{ocaml_libdir}/xapi-tapctl/*.a
%exclude %{ocaml_libdir}/xapi-tapctl/*.cmxa
%exclude %{ocaml_libdir}/xapi-tapctl/*.cmxs
%exclude %{ocaml_libdir}/xapi-tapctl/*.cmx
%exclude %{ocaml_libdir}/xapi-tapctl/*.mli
%exclude %{ocaml_libdir}/xapi-tapctl/*.cmt
%exclude %{ocaml_libdir}/xapi-tapctl/*.cmti

%files devel
%{ocaml_libdir}/xapi-tapctl/*.a
%{ocaml_libdir}/xapi-tapctl/*.cmx
%{ocaml_libdir}/xapi-tapctl/*.cmxa
%{ocaml_libdir}/xapi-tapctl/*.cmxs
%{ocaml_libdir}/xapi-tapctl/*.mli
%{ocaml_docdir}/xapi-tapctl

%changelog
* Mon Jun 03 2024 Gael Duperrey <gduperrey@vates.tech> - 1.5.1-15.1
- Rebuild after sync with hotfix XS82ECU1064
- No source changes: only rebuild for dependencies
- *** Upstream changelog ***
- * Fri Mar 08 2024 Christian Lindig <christian.lindig@cloud.com> - 1.5.1-15
- - Bump release and rebuild
- * Wed Mar 06 2024 Christian Lindig <christian.lindig@cloud.com> - 1.5.1-14
- - Bump release and rebuild
- * Tue Mar 05 2024 Christian Lindig <christian.lindig@cloud.com> - 1.5.1-13
- - Bump release and rebuild
- * Fri Nov 03 2023 Christian Lindig <christian.lindig@cloud.com> - 1.5.1-12
- - Bump release and rebuild
- * Tue Oct 24 2023 Christian Lindig <christian.lindig@cloud.com> - 1.5.1-11
- - Bump release and rebuild
- * Tue Oct 24 2023 Christian Lindig <christian.lindig@cloud.com> - 1.5.1-10
- - Bump release and rebuild
- * Wed Oct 18 2023 Christian Lindig <christian.lindig@cloud.com> - 1.5.1-9
- - Bump release and rebuild

* Fri Oct 13 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.5.1-8.1
- Rebuild after sync with hotfix XS82ECU1049
- No source changes: only rebuild for dependencies
- *** Upstream changelog ***
- * Mon Oct 02 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 1.5.1-8
- - Bump release and rebuild

* Wed Aug 09 2023 Gael Duperrey <gduperrey@vates.fr> - 1.5.1-7.1
- Sync with hotfix XS82ECU1040
- *** Upstream changelog ***
- * Thu Jul 20 2023 Rob Hoes <rob.hoes@citrix.com> - 1.5.1-7
- - Bump release and rebuild
- * Mon Jun 19 2023 Christian Lindig <christian.lindig@citrix.com> - 1.5.1-6
- - Bump release and rebuild
- * Thu Jun 08 2023 Christian Lindig <christian.lindig@citrix.com> - 1.5.1-5
- - Bump release and rebuild
- * Fri May 12 2023 Christian Lindig <christian.lindig@citrix.com> - 1.5.1-4
- - Bump release and rebuild
- * Fri May 12 2023 Christian Lindig <christian.lindig@citrix.com> - 1.5.1-3
- - Bump release and rebuild

* Fri Apr 14 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.5.1-2.1
- *** Upstream changelog ***
- * Thu Feb 23 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 1.5.1-2
- - Change license to match source repo
- * Mon Feb 20 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 1.5.1-1
- - Same as 1.5.0, koji tooling needed an annotated tag to build

* Wed Oct 12 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.5.0-5.3
- Rebuild for security update synced from XS82ECU1019$

* Wed Aug 17 2022 Gael Duperrey <gduperrey@vates.fr> - 1.5.0-5.2
- Rebuild for updated xapi from XS82ECU1011

* Mon Dec 20 2021 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.5.0-5.1
- Sync with CH 8.2.1
- *** Upstream changelog ***
- * Mon Sep 27 2021 Pau Ruiz Safont <pau.safont@citrix.com> - 1.5.0-5
- - Bump package after xs-opam update
- * Tue Jul 13 2021 Edwin Török <edvin.torok@citrix.com> - 1.5.0-4
- - bump packages after xs-opam update

* Thu Sep 02 2021 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.5.0-3.3
- Rebuild for message-switch 1.23.1 and rebuilt forkexecd from XS82E031

* Tue May 18 2021 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.5.0-3.2
- Rebuild for xs-opam-repo 6.35.6 and rebuilt forkexecd from XS82E020

* Thu Nov 05 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.5.0-3.1
- Rebuild for xs-opam-src 6.35.1 from XS82E002

* Fri Aug 23 2019 Edwin Török <edvin.torok@citrix.com> - 1.5.0-2
- bump packages after xs-opam update

* Thu Aug 15 2019 Christian Lindig <christian.lindig@citrix.com> - 1.5.0-1
- maintenance: use rpclib instead of rpc
- travis: update variables

* Thu Nov 22 2018 Christian Lindig <christian.lindig@citrix.com> - 1.4.0-1
- Completed port to dune.

* Thu Nov 01 2018 Christian Lindig <christian.lindig@citrix.com> - 1.3.0-1
- Update Opam and Travis setup

* Tue Sep 18 2018 Christian Lindig <christian.lindig@citrix.com> - 1.2.0-1
- Simplify jbuild for PPX processing
- Use Re.Str instead of deprecated Re_str

* Wed Apr 04 2018 Marcello Seri <marcello.seri@citrix.com> - 1.1.0-6
- Update SPEC file to get rid of rpmbuild warnings

* Wed Jan 10 2018 Konstantina Chremmou <konstantina.chremmou@citrix.com> - 1.1.0-1
- Ported build from oasis to jbuilder

* Mon Mar 13 2017 Marcello Seri <marcello.seri@citrix.com> - 1.0.1-2
- Update OCaml dependencies and build/install script after xs-opam-repo split

* Wed Jun 22 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.0.1-1
- Update to 1.0.1

* Thu Apr 21 2016 Euan Harris <euan.harris@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Sat Apr 4 2015 David Scott <dave.scott@citrix.com> - 0.10.0-1
- Update to 0.10.0

* Fri Jun 6 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.2-1
- Update to 0.9.2

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.9.1-2
- Split files correctly between base and devel packages

* Fri Oct 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-1
- Update to 0.9.1

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

