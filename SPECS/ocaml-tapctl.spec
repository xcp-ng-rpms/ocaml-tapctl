%global debug_package %{nil}

Name:           ocaml-tapctl
Version:        1.5.0
Release:        3.2%{?dist}
Summary:        Manipulate running tapdisk instances
License:        LGPL
URL:            https://github.com/xapi-project/tapctl

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/tapctl/archive?at=v1.5.0&format=tar.gz&prefix=ocaml-tapctl-1.5.0#/tapctl-1.5.0.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/tapctl/archive?at=v1.5.0&format=tar.gz&prefix=ocaml-tapctl-1.5.0#/tapctl-1.5.0.tar.gz) = 6827cad4bebd3e2fbd289a469231bf7570f265d2

BuildRequires:  xs-opam-repo
BuildRequires:  forkexecd-devel

%global _use_internal_dependency_generator 0
%global __requires_exclude *caml*

%description
Manipulate running tapdisk instances on a xen host.

%package        devel
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/tapctl/archive?at=v1.5.0&format=tar.gz&prefix=ocaml-tapctl-1.5.0#/tapctl-1.5.0.tar.gz) = 6827cad4bebd3e2fbd289a469231bf7570f265d2
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

