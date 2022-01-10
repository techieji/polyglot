package polyglotj;

public class Message {
	private String purpose;
	private String from;
	private String to;
	private Object data;
	Message() {}
	Message(String p, String f, String t, Object d) { purpose = p; from = f; to = t; data = d; }
	public String getPurpose() { return purpose; }
	public String getFrom()    { return from; }
	public String getTo()      { return to; }
	public Object getData()    { return data; }
	public void setPurpose(String v) { purpose = v; }
	public void setFrom(String v)    { from = v; }
	public void setTo(String v)      { to = v; }
	public void setData(Object v)    { data = v; }
}
