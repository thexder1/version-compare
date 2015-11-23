# version-compare

Basic library for comparing semantic versions. Contains a versionCompare function
that accepts arguments of current version, version to compare against, and the
comparison operator. Usage example is below.

```
from versionCompare import VersionCompare as vc

currentVersion = '1.0.0'
comparisonVersion = '1.0.0'
if vc.versionCompare(currentVersion, comparisonVersion, '=='):
  print 'versions are equal'
```
