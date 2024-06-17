{{config(materialized='view')}}


with source_data as (

select *
from {{ public('DoctorsET') }}
where msg_id = 864

)
