import collections
import copy
from .Utils import _write_complex_object
from .DataPointType import DataPointType
from .DependencyKind import DependencyKind
from .DependencySourceType import DependencySourceType

class RemoteDependencyData(object):
    """Data contract class for type RemoteDependencyData.
    """
    ENVELOPE_TYPE_NAME = 'Microsoft.ApplicationInsights.RemoteDependency'
    
    DATA_TYPE_NAME = 'RemoteDependencyData'
    
    _defaults = collections.OrderedDict([
        ('ver', 2),
        ('id', None),
        ('name', None),
        ('data', None),
        ('type', DependencyKind.undefined),
        ('duration', None),
        ('target', None),
        ('success', None),
        ('resultCode', None),
        ('properties', {}),
        ('measurements', {}),
    ])
    
    def __init__(self):
        """Initializes a new instance of the class.
        """
        self._values = {
            'ver': 2,
            'name': None,
            'data': None,
            'type': DependencyKind.undefined,
            'duration': None,
            'target': None,
            'success': None,
            'resultCode': None,
        }
        self._initialize()

    @property
    def name(self):
        """The name property.

        Returns:
            (string). the property value. (defaults to: None)
        """
        return self._values['name']

    @name.setter
    def name(self, value):
        """The name property.

        Args:
            value (string). the property value.
        """
        self._values['name'] = value

    @property
    def id(self):
        """The id property.

        Returns:
            (int). the property value. (defaults to: None)
        """
        if 'id' in self._values:
            return self._values['id']
        return self._defaults['id']

    @id.setter
    def id(self, value):
        """The id property.

        Args:
            value (int). the property value.
        """
        if value == self._defaults['id'] and 'id' in self._values:
            del self._values['id']
        else:
            self._values['id'] = value

    @property
    def duration(self):
        return self._values['duration']

    @duration.setter
    def duration(self, value):
        """The name property.

        Args:
            value (string). the property value.
        """
        self._values['duration'] = value

    @property
    def target(self):
        return self._values['target']

    @target.setter
    def target(self, value):
        if value == self._defaults['target'] and 'target' in self._values:
            del self._values['target']
        else:
            self._values['target'] = value

    @property
    def result_code(self):
        return self._values['resultCode']

    @result_code.setter
    def result_code(self, value):
        """The name property.

        Args:
            value (string). the property value.
        """
        self._values['resultCode'] = value

    @property
    def data(self):
        """Gets or sets data associated with the current dependency instance. Command name/statement for SQL dependency, URL for http dependency.

        Returns:
            (string). the property value. (defaults to: None)
        """
        return self._values['data']

    @data.setter
    def data(self, value):
        """Gets or sets data associated with the current dependency instance. Command name/statement for SQL dependency, URL for http dependency.

        Args:
            value (string). the property value.
        """
        self._values['data'] = value

    @property
    def type(self):
        if 'type' in self._values:
            return self._values['type']
        return self._defaults['type']
        
    @type.setter
    def type(self, value):
        if value == self._defaults['type'] and 'type' in self._values:
            del self._values['type']
        else:
            self._values['type'] = value

    @property
    def success(self):
        """The success property.
        
        Returns:
            (bool). the property value. (defaults to: True)
        """
        if 'success' in self._values:
            return self._values['success']
        return self._defaults['success']
        
    @success.setter
    def success(self, value):
        """The success property.
        
        Args:
            value (bool). the property value.
        """
        if value == self._defaults['success'] and 'success' in self._values:
            del self._values['success']
        else:
            self._values['success'] = value

    @property
    def properties(self):
        """The properties property.
        
        Returns:
            (hash). the property value. (defaults to: {})
        """
        if 'properties' in self._values:
            return self._values['properties']
        self._values['properties'] = copy.deepcopy(self._defaults['properties'])
        return self._values['properties']
        
    @properties.setter
    def properties(self, value):
        """The properties property.
        
        Args:
            value (hash). the property value.
        """
        if value == self._defaults['properties'] and 'properties' in self._values:
            del self._values['properties']
        else:
            self._values['properties'] = value

    @property
    def measurements(self):
        """The measurements property.

        Returns:
            (hash). the property value. (defaults to: {})
        """
        if 'measurements' in self._values:
            return self._values['measurements']
        self._values['measurements'] = copy.deepcopy(self._defaults['measurements'])
        return self._values['measurements']

    @measurements.setter
    def measurements(self, value):
        """The measurements property.

        Args:
            value (hash). the property value.
        """
        if value == self._defaults['measurements'] and 'measurements' in self._values:
            del self._values['measurements']
        else:
            self._values['measurements'] = value

    def _initialize(self):
        """Initializes the current instance of the object."""
        pass
    
    def write(self):
        """Writes the contents of this object and returns the content as a dict object.
        
        Returns:
            (dict). the object that represents the same data as the current instance.
        """
        return _write_complex_object(self._defaults, self._values)
