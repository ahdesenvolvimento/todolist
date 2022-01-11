export default function Input({ text, name, type, placeholder, handleOnChange}){
    return (
        <div className="form-floating mb-3">
            <input type={type} name={name} onChange={handleOnChange} className="form-control" placeholder={placeholder}/>
            <label htmlFor={name}>{text}</label>
        </div>
    )
}