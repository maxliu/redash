
import sys
sys.path.append("/app/")
sys.path.append("/app/redash/")
from intersyscache import InterSysCache



sql = """

select *
from IRISDemo_Data.Appointment
-- where 1=0
"""

configuration={'dbpath':''}

ic = InterSysCache(configuration)

data = ic.run_query(sql,'max')
print(data)