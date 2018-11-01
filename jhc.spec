Summary: Jhc Haskell Compiler
Name: jhc
Version: 0.8.2
Release: 1
License: COPYING
Group: Development/Languages/Haskell
BuildRoot: %{_tmppath}/%{name}-root
Source: http://repetae.net/dist/%{name}-%{version}.tar.gz
URL: http://repetae.net/computer/jhc/
Packager: John Meacham <john@repetae.net>
Prefix: %{_prefix}
BuildRequires: ghc-editline-devel, ghc-binary-devel,  haskell-platform, ghc, ghc-zlib-devel, ghc-utf8-string-devel

%description
Jhc Haskell compiler.

%prep
%setup

%build
%configure
make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT



%files
%defattr(-,root,root)
%{_bindir}/jhc
%{_bindir}/jhci
%{_mandir}/man1/jhc.1.gz

%{_datadir}/jhc-0.8/jhc-prim-1.0.hl
%{_datadir}/jhc-0.8/jhc-1.0.hl
%{_datadir}/jhc-0.8/base-1.0.hl
%{_datadir}/jhc-0.8/haskell98-1.0.hl
%{_datadir}/jhc-0.8/flat-foreign-1.0.hl
%{_datadir}/jhc-0.8/applicative-1.0.hl
%{_datadir}/jhc-0.8/containers-0.3.0.0.hl
%{_datadir}/jhc-0.8/Diff-0.1.2.hl
%{_datadir}/jhc-0.8/html-1.0.1.2.hl
%{_datadir}/jhc-0.8/HUnit-1.2.2.1.hl
%{_datadir}/jhc-0.8/pretty-1.0.1.1.hl
%{_datadir}/jhc-0.8/safe-0.2.hl
%{_datadir}/jhc-0.8/smallcheck-0.4.hl
%{_datadir}/jhc-0.8/xhtml-3000.2.0.1.hl
%{_datadir}/jhc-0.8/QuickCheck-1.2.0.0.hl
%{_datadir}/jhc-0.8/parsec-2.1.0.1.hl
%{_datadir}/jhc-0.8/transformers-0.2.1.0.hl
%{_datadir}/jhc-0.8/filepath-1.2.0.0.hl
%{_datadir}/jhc-0.8/deepseq-1.1.0.2.hl
%{_datadir}/jhc-0.8/include/HsFFI.h
%{_sysconfdir}/jhc-0.8/targets.ini

%doc COPYING


