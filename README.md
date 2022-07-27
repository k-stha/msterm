# msterm

A simple terminal emulator using VTE and GTK

## Table of Contents

- [Dependencies](#dependencies)
  - [For Arch and Arch based distributions](#for-arch-and-arch-based-distributions)
  - [For Debian and Debian based distributions](#for-debian-and-debian-based-distributions)
- [Considerations](#considerations)
- [Contribution Guidelines](#contribution-guidelines)

## Dependencies

### For Arch and Arch based distributions

- vte3
- python-gobject

### For Debian and Debian based distributions

- gir1.2-vte-2.91
- python3-gi

## Considerations

This terminal emulator is not (currently) capable of protecting users from
unsafe copy-paste from sources like websites (See:
[Copy-Paste from Website to Terminal](https://thejh.net/misc/website-terminal-copy-paste)).

## Contribution Guidelines

See [CONTRIBUTING.md](CONTRIBUTING.md)
