-- 1113试乘试驾报表

/*
SELECT 
  tdssr.`id` as 'id',
  tdssr.`date` as '日期',
  tdssr.shop_code as '经销商代码',
  s.series_name as '车系',
  cc.name as '一级渠道',
  tdssr.`oringinal_customer_num` as '原始线索(线索表)',
  tdssr.`valid_customer_num` as '有效线索',
  tdssr.`customer_level_h_a_b_num` as '等级为H, A, B的客户数量',
  tdssr.`first_into_store_num` as '首次客流',
  tdssr.`non_first_into_store_num` as '非首次客流',
  tdssr.`total_into_store_num` as '总客流',
  tdssr.`valid_test_drive_num` as  '有效试乘试驾客流',
  tdssr.`test_drive_num` as '试乘试驾数量',
  tdssr.`order_num` as '包含大客户订单，按照通过审批的时间进行计算',
  tdssr.`first_into_store_order` as '首次客流订单',
  tdssr.`current_month_cancel_order_num` as '退订当月订单',
  tdssr.`history_cancel_order_num` as '退订历史订单',
  tdssr.`delivery_num` as '交车数',
  tdssr.`original_customer_num_cus` as 'customer表的线索数'
FROM infiniti_service.t_data_statistics_saler_report as tdssr
left JOIN souche_crm.clue_category as cc on tdssr.`first_source`=cc.code
left JOIN car_model.series as s ON s.series_code=tdssr.`series_code`
WHERE 
DATE_FORMAT(tdssr.date,'%Y-%m-%d')='2018-10-30' and 
tdssr.shop_code='LHJDP001';
*/

SELECT 
  tdssr.`id` as 'id',
  tdssr.`date` as '日期',
  tdssr.shop_code as '经销商代码',
  s.series_name as '车系',
  cc.name as '一级渠道',
  tdssr.`valid_test_drive_num` as  '有效试乘试驾客流',
  tdssr.`first_into_store_order` as '首次客流订单'
FROM infiniti_service.t_data_statistics_saler_report as tdssr
left JOIN souche_crm.clue_category as cc on tdssr.`first_source`=cc.code
left JOIN car_model.series as s ON s.series_code=tdssr.`series_code`
WHERE 
DATE_FORMAT(tdssr.date,'%Y-%m-%d')='2018-11-01' and 
tdssr.shop_code='HFGP001';


-- 有效的试乘试驾客流

SELECT 
		DISTINCT
		ac.sc,-- 店铺code
		ac.sn ,-- 车系名称
		ac.name,-- 一级来源
                count(*) as '有效的试乘试驾客流',
		ac.fdc -- 跟进时间
FROM 
(
	SELECT 
		DISTINCT
		f.customer_id as ci,
		c.phone,
		cc.name,
		c.shop_code as sc,
		s.series_name as sn,
		edc.car_serial_code as csc,
		c.first_source as fs,		
		date_format(f.date_create,'%Y-%m-%d')  as fdc
	from souche_crm.follow as f 
	left JOIN souche_crm.customer as c ON f.customer_id=c.id
	left JOIN souche_crm.clue_category as cc on c.first_source=cc.code
	left JOIN souche_crm.buy_car_demand_brand_series as bcdbs ON bcdbs.customer_id=c.id 
	left JOIN car_model.series as s ON s.series_code=bcdbs.series
        inner JOIN infiniti_service.econtract_driver_car as edc ON edc.car_serial_code=s.series_code AND edc.`status`=1 AND c.shop_code=edc.dms_dealer_code
        
	WHERE f.date_create between '2018-11-01 00:00:00' and '2018-11-01 23:59:59'
	and f.communication_type='arrive'
	and f.shop_code='HFGP001'
	ORDER BY f.date_create ASC
)ac
GROUP BY
ac.sc,
ac.sn,
ac.fs,
ac.fdc
ORDER BY fdc;




SELECT 
		DISTINCT
		ac.sc,-- 店铺code
		ac.sn ,-- 车系名称
		ac.name,-- 一级来源
ac.ssc,
ac.cp,
		ac.fdc -- 跟进时间
FROM 
(
	SELECT 
		DISTINCT
		f.customer_id as ci,
		c.phone as cp,
		cc.name,
		c.shop_code as sc,
		s.series_code as ssc,
		s.series_name as sn,
		-- edc.car_serial_code as csc,
		c.first_source as fs,		
		date_format(f.date_create,'%Y-%m-%d')  as fdc
	from souche_crm.follow as f 
	left JOIN souche_crm.customer as c ON f.customer_id=c.id
	left JOIN souche_crm.clue_category as cc on c.first_source=cc.code
	left JOIN souche_crm.buy_car_demand_brand_series as bcdbs ON bcdbs.customer_id=c.id 
	left JOIN car_model.series as s ON s.series_code=bcdbs.series
        -- inner JOIN infiniti_service.econtract_driver_car as edc ON edc.car_serial_code=s.series_code AND edc.`status`=1 AND c.shop_code=edc.dms_dealer_code
        
	WHERE f.date_create between '2018-10-30 00:00:00' and '2018-10-30 23:59:59'
	and f.communication_type='arrive'
	and f.shop_code='HFGP001'
	ORDER BY f.date_create ASC
)ac
ORDER BY fdc;



-- 首次客流订单
SELECT 
	oi.shop_code as sc,
	m.series_name as sn,
	cc.`name` as cn,
	count(*) as '首次客流订单',
	DATE_FORMAT(toa.create_end_time,'%Y-%m-%d')  as cet
	/*oi.order_code as '订单编号',
	oi.order_status as '订单状态',
	toa.create_audit_status as '审批状态'*/
	
from infiniti_service.t_order_info as oi
left JOIN infiniti_service.t_order_audit as toa ON toa.order_code=oi.order_code -- 订单审批表
left JOIN infiniti_service.t_order_customer as toc ON toc.order_code=oi.order_code
left JOIN souche_crm.customer as c ON c.crm_user_id=toc.user_code and oi.shop_code=c.shop_code
INNER JOIN souche_crm.customer_sub as cs ON cs.customer_id=c.id AND DATE_FORMAT(oi.create_time,'%Y-%m-%d')=DATE_FORMAT(cs.first_arrive_time,'%Y-%m-%d')  
left JOIN souche_crm.clue_category as cc on c.first_source=cc.code 
left JOIN car_model.model as m ON m.model_code=oi.car_model_code

WHERE toa.create_end_time between '2018-10-30 00:00:00' and '2018-10-30 23:59:59' -- 审批通过的时间
and toa.create_audit_status='agree' 
AND oi.shop_code='HFGP001'
GROUP BY
sc,sn,cn,cet
ORDER BY cet ASC; 



SELECT 
	oi.shop_code as sc,
	m.series_name as sn,
	cc.`name` as cn,
c.phone,
	DATE_FORMAT(toa.create_end_time,'%Y-%m-%d')  as cet
	/*oi.order_code as '订单编号',
	oi.order_status as '订单状态',
	toa.create_audit_status as '审批状态'*/

	
from infiniti_service.t_order_info as oi
left JOIN infiniti_service.t_order_audit as toa ON toa.order_code=oi.order_code -- 订单审批表
left JOIN infiniti_service.t_order_customer as toc ON toc.order_code=oi.order_code
left JOIN souche_crm.customer as c ON c.crm_user_id=toc.user_code and oi.shop_code=c.shop_code
INNER JOIN souche_crm.customer_sub as cs ON cs.customer_id=c.id AND DATE_FORMAT(oi.create_time,'%Y-%m-%d')=DATE_FORMAT(cs.first_arrive_time,'%Y-%m-%d')  
left JOIN souche_crm.clue_category as cc on c.first_source=cc.code 
left JOIN car_model.model as m ON m.model_code=oi.car_model_code

WHERE toa.create_end_time between '2018-10-30 00:00:00' and '2018-10-30 23:59:59' -- 审批通过的时间
and toa.create_audit_status='agree' 
AND oi.shop_code='HFGP001'
ORDER BY cet ASC; 

