# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`num2words` is a Python library that converts numbers to words in multiple languages. It supports cardinal numbers, ordinal numbers, currency conversion, and year formatting across 50+ languages.

## Architecture

### Class Hierarchy

The project uses a base class inheritance pattern:

```
Num2Word_Base (base.py)
  └── Num2Word_EU (lang_EU.py) - European language base class
       └── Language-specific classes (e.g., Num2Word_ES, Num2Word_CA, Num2Word_EUS)
```

**Important**: `lang_EU.py` contains the European language base class, NOT Basque/Euskera. Basque is implemented in `lang_EUS.py` and registered as 'eu' in `__init__.py`.

### Module Structure

- **`base.py`**: Core `Num2Word_Base` class with common conversion logic
- **`lang_EU.py`**: European language base with currency forms and helper methods
- **`lang_XX.py`**: Individual language implementations (XX = language code in caps)
- **`__init__.py`**: Registers all languages in `CONVERTER_CLASSES` dict with lowercase keys
- **`currency.py`**: Currency parsing utilities
- **`compat.py`**: Python 2/3 compatibility helpers

## Testing

### Run all tests
```bash
python3 -m unittest discover
```

### Run tests for a specific language
```bash
python3 -m unittest tests.test_eu -v
```

### Run full CI suite (linting + multi-env tests)
```bash
pip install tox
tox
```

### Coverage requirements
- Main code: 75% minimum
- Test code: 100% minimum

### Linting
```bash
# PEP8 compliance
tox -e flake8

# Import ordering
tox -e isort
```

## Adding a New Language

When adding a new language, follow this workflow:

1. **Create language file**: `num2words/lang_XXX.py` (use 2-letter ISO code or 3-letter if conflict exists)
   - Inherit from `Num2Word_EU` or `Num2Word_Base`
   - Implement `setup()` method with number words
   - Implement `merge()` method for number combination logic
   - Implement `to_ordinal()` and `to_ordinal_num()` methods
   - Define `CURRENCY_FORMS` dict if supporting currency

2. **Register in `__init__.py`**:
   - Add import in imports section
   - Add entry to `CONVERTER_CLASSES` with lowercase key

3. **Create test file**: `tests/test_xx.py`
   - Define `TEST_CASES_CARDINAL` with comprehensive number coverage
   - Define `TEST_CASES_ORDINAL` if applicable
   - Define `TEST_CASES_ORDINAL_NUM` if applicable
   - Define `TEST_CASES_TO_CURRENCY` if applicable
   - Create test class inheriting from `unittest.TestCase`

4. **Verify**:
   ```bash
   python3 -m unittest tests.test_xx -v
   ```

### Language File Naming Convention

- File name: `lang_XX.py` (uppercase language code)
- Class name: `Num2Word_XX` (matches file)
- Registry key: `'xx'` (lowercase in `__init__.py`)

Example: Basque uses `lang_EUS.py` (file), `Num2Word_EUS` (class), `'eu'` (registry key) because `lang_EU.py` already exists as the European base class.

## Key Implementation Patterns

### Number Words Structure

Language implementations define three key lists in `setup()`:

- **`low_numwords`**: 0-29 (reverse order: 29, 28, ..., 0)
- **`mid_numwords`**: Tuples of (value, word) for 30+, 100, 1000, etc.
- **`ords`**: Dict mapping numbers to ordinal words

### Merge Logic

The `merge()` method combines number parts. Common patterns:

- Check if current number is 1 (often omitted in speech)
- Handle smaller + larger (e.g., 30 + 4 = 34)
- Handle larger * smaller (e.g., 2 * 100 = 200)
- Language-specific concatenation (spaces, hyphens, contractions)

### Currency Support

Define `CURRENCY_FORMS` dict with structure:
```python
'EUR': (('singular', 'plural'), ('cent_singular', 'cent_plural'))
```

## Code Style

- Must be PEP8 compliant
- Use `flake8` for linting
- Use `isort` for import ordering with `--float-to-top` flag
- Include copyright header in all new files
- Support Python 3.7+

## Common Pitfalls

1. **Name conflicts**: Check existing files before naming (e.g., `lang_EU.py` exists as base class)
2. **Registry key case**: Always use lowercase in `CONVERTER_CLASSES` dict
3. **low_numwords order**: Must be in reverse (highest to lowest)
4. **Merge logic**: Test edge cases like 1, 100, 1000 as they often need special handling
5. **Import location**: Add language imports alphabetically in `__init__.py`
