Generate random Belgian VAT numbers with valid checksums.

**Usage:** python be_vat.py [count] [--invalid]

*--invalid*: Create wrong checksum, for negative testing.

**Examples**
| command                      | Description                                                  |
|------------------------------|--------------------------------------------------------------|
| python be_vat.py             | prints 10 valid numbers.                                     |
| python be_vat.py 50          | prints 50 valid numbers.                                     |
|python be_vat.py 20 --invalid | prints 20 numbers with a wrong checksum, for negative tests. |
