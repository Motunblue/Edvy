import './header.css';

export default function Header() {
  return (
      <header>
        <div className="logo">
          <p>Edvy</p>
          {/* <img src="" className="App-logo" alt="logo" /> */}
        </div>
        <div className="header-nav">
            <h4 className='login'>login
              <div className='login-as'>
                <p className="user-login">user</p>
                <p className="admin-login">admin</p>
              </div>
            </h4>
            <h4 className='sign-up'/*  onClick={signupClick} */>sign-up</h4>
        </div>
      </header>
  );
}
